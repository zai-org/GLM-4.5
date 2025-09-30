# GLM-4.6 Tool-Integrated Reasoning Guide

The tool call process of **GLM-4.6** follows the workflow below:

1. Provide the function definitions of the available tools to the GLM-4.6 model.  
2. GLM-4.6 autonomously decides whether a tool call is necessary based on the user request and returns the corresponding call parameters if a tool call is made.  
3. The user executes the actual tool call and returns the execution results to the model.  
4. GLM-4.6 continues generating responses based on the tool execution results, repeating the above process until enough information is obtained to complete the user’s request.  

## Automatic Parsing of Reasoning and Tool Calls

To enable the inference engine to utilize **automatic reasoning and tool call parser**, the service should be started with the appropriate parameters. For example, when launching with **sglang**:

```bash
python3 -m sglang.launch_server \
  --model-path zai-org/GLM-4.6 \
  --tp-size 8 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.7 \
  --served-model-name glm-4.6 \
  --host 0.0.0.0 \
  --port 8000
````


### Tools Definitions

**GLM-4.6** comes with a set of built-in tools:
* **python** – Python code interpreter
* **browser.search** – Web search
* **browser.open** – Open a webpage link
* **browser.find** – Search content within the opened webpage

```python
tools = [
    {
        "type": "function",
        "function":{
            "name": "python",
            "description": "Interpreter for executing python code",
            "parameters": {
                "type": "object",
                "properties": {"code": {"description": "Code to execute", "type": "string"}},
            },
        }
    },
    {
        "type": "function",
        "function":{
            "name": "browser.search",
            "description": "Search in browser",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"description": "Search query", "type": "string"},
                    "num": {"description": "Number of results to return", "type": "integer", "default": 10},
                },
                "required": ["query"],
            },
        }
    },
    {
        "type": "function",
        "function":{
            "name": "browser.open",
            "description": "Open browser link",
            "parameters": {
                "type": "object",
                "properties": {
                    "id": {"description": "ID or URL of the link to open", "type": ["integer", "string"]},
                },
                "required": ["id"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "browser.find",
            "description": "Find pattern in the opened browser content",
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"description": "Pattern to find", "type": "string"},
                },
                "required": ["pattern"],
            },
        }
    },
]
```

### Tools Implementations

```python
def python_tool(code: str) -> str:
    # Your implementation of the python tool
    return f"Result of python execution."

def search_tool(query: str, num: int = 10) -> str:
    # Your implementation of the search tool
    return f"Search results for query."

def open_tool(id) -> str:
    # Your implementation of the open tool
    return f"Opened result."

def find_tool(pattern: str) -> str:
    # Your implementation of the find tool
    return f"Found pattern."

tool_map = {
    "python": python_tool,
    "browser.search": search_tool,
    "browser.open": open_tool,
    "browser.find": find_tool,
}
```


### Model Request

```python
import requests
import json

api_base = "http://ip:port/v1"

messages = [
    {"role": "user", "content": "Calculate the 1000th term of the Fibonacci sequence."},
]

finish_reason = None
while finish_reason is None or finish_reason == "tool_calls":
    request_data = {
        "model": "glm-4.6",
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 1.0,
        "stop": ["<|user|>", "<|endoftext|>", "<|observation|>", "<|assistant|>"],
        "tools": tools,
        "stream": False,
    }
    response = requests.post(
        f"{api_base}/chat/completions",
        headers={"Content-Type": "application/json"},
        json=request_data
    )
    response.raise_for_status()
    response_json = response.json()
    choice = response_json["choices"][0]
    finish_reason = choice["finish_reason"]
    if finish_reason == "tool_calls":
        messages.append(choice["message"])
        tool_calls = choice["message"]["tool_calls"]
        for tool_call in tool_calls:
            tool_name = tool_call["function"]["name"]
            tool_arguments = json.loads(tool_call["function"]["arguments"])
            tool_call_id = tool_call["id"]
            
            tool_output = tool_map[tool_name](**tool_arguments)
            
            messages.append({
                "role": "tool",
                "name": tool_name,
                "content": tool_output,
                "tool_call_id": tool_call_id,
            })
print(choice["message"]["content"])
```


## Manual Parsing of Reasoning and Tool Calls

On services that do not provide `reasoning-parser` and `tool-call-parser`, the response generated by GLM-4.6 can be parsed **manually**.

* The reasoning content generated by GLM-4.6 is wrapped with `<think>` and `</think>`.
* Each tool call is wrapped with `<tool_call>` and `</tool_call>`.
* The function name immediately follows `<tool_call>`.
* Parameters are wrapped with `<arg_key>` and `<arg_value>`.

Thus, you can directly send requests to the **completions API** and manually parse out reasoning content, function names, arguments, etc.


## Parsing Code

The function `parse_model_response` can parse the output of GLM-4.6 and return reasoning content and tool call information.

```python
import re
import json
import uuid

def parse_arguments(json_value):
    try:
        parsed_value = json.loads(json_value)
        return parsed_value, isinstance(parsed_value, dict)
    except:
        return json_value, False

def get_argument_type(func_name: str, arg_key: str, defined_tools: list):
    name2tool = {tool["name"]: tool for tool in defined_tools}
    if func_name not in name2tool:
        return None
    tool = name2tool[func_name]
    if arg_key not in tool["parameters"]["properties"]:
        return None
    return tool["parameters"]["properties"][arg_key]["type"]

def parse_model_response(response: str, defined_tools: list):
    text = response.strip()
    reasoning_content = None
    content = None
    tool_calls = []
    
    # reasoning_content
    if text.startswith('<think>'):
        if '</think>' in text:
            reasoning_content, text = text.rsplit('</think>', 1)
            reasoning_content = reasoning_content.removeprefix('<think>').strip()
            text = text.strip()
        else:
            reasoning_content = text.removeprefix('<think>').strip()
            text = ""
    
    # content      
    if '<tool_call>' in text:
        index = text.find('<tool_call>')
        content = text[:index].strip()
        text = text[index:].strip()
    else:
        content = text.strip()
        text = ""
    
    # tool_calls
    tool_call_strs = re.findall(r'<tool_call>(.*?)</tool_call>', text, re.DOTALL)
    for call in tool_call_strs:
        func_name_match = re.match(r'([^\n<]+)', call.strip())
        func_name = func_name_match.group(1).strip() if func_name_match else None
        if func_name:
            pairs = re.findall(r'<arg_key>(.*?)</arg_key>\s*<arg_value>(.*?)</arg_value>', call, re.DOTALL)
            arguments = {}
            for arg_key, arg_value in pairs:
                arg_key = arg_key.strip()
                arg_value = arg_value.strip()
                arg_type = get_argument_type(func_name, arg_key, defined_tools)
                if arg_type != 'string':
                    arg_value, is_good_json = parse_arguments(arg_value)
                arguments[arg_key] = arg_value
                
            tool_calls.append({
                'tool_call_id': "tool-call-" + str(uuid.uuid4()),
                'name': func_name,
                'arguments': arguments
            })
    
    message = {'role': 'assistant'}
    if reasoning_content:
        message['reasoning_content'] = reasoning_content
    if content:
        message['content'] = content
    if tool_calls:
        message['tool_calls'] = tool_calls
    
    return message
```

---

### Model Request

```python
from transformers import AutoTokenizer
import json
import requests

api_base = "http://ip:port/v1"

tools = [
    {
        "name": "python",
        "description": "Interpreter for executing python code",
        "parameters": {
            "type": "object",
            "properties": {"code": {"description": "Code to execute", "type": "string"}},
        },
    },
    {
        "name": "browser.search",
        "description": "Search in browser",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"description": "Search query", "type": "string"},
                "num": {"description": "Number of results to return", "type": "integer", "default": 10},
            },
            "required": ["query"],
        },
    },
    {
        "name": "browser.open",
        "description": "Open browser link",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {"description": "ID or URL of the link to open", "type": ["integer", "string"]},
            },
            "required": ["id"],
        },
    },
    {
        "name": "browser.find",
        "description": "Find pattern in the opened browser content",
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"description": "Pattern to find", "type": "string"},
            },
            "required": ["pattern"],
        },
    },
]

tokenizer = AutoTokenizer.from_pretrained("zai-org/GLM-4.6", trust_remote_code=True)

messages = [
    {"role": "user", "content": "Calculate the 1000th term of the Fibonacci sequence."},
]

while True:
    prompt = tokenizer.apply_chat_template(messages, tools, add_generation_prompt=True, tokenize=False)
    request_data = {
        "model": "glm-4.6",
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 1.0,
        "stop": ["<|user|>", "<|endoftext|>", "<|observation|>", "<|assistant|>"],
        "stream": False,
    }
    response = requests.post(
        f"{api_base}/completions",
        headers={"Content-Type": "application/json"},
        json=request_data,
        timeout=360
    )
    response_json = response.json()
    text = response_json["choices"][0]["text"]
    assistant_message = parse_model_response(text, tools)
    messages.append(assistant_message)
    tool_calls = assistant_message.get("tool_calls", [])
    if not tool_calls:
        break
    for tool_call in tool_calls:
        tool_name = tool_call["name"]
        tool_arguments = tool_call["arguments"]

        tool_output = tool_map[tool_name](**tool_arguments)
        messages.append({
                "role": "tool",
                "name": tool_name,
                "content": tool_output,
                "tool_call_id": tool_call["tool_call_id"],
        })     
print(assistant_message)
```
