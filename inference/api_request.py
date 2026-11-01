from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://127.0.0.1:8000/v1"
import json

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        },
    },
]
messages = [
    {"role": "system", "content": "请你调用工具，用中文回答问题。"},
    {"role": "user", "content": "请帮我查询一下北京的天气。"},
]

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
completion = client.chat.completions.create(
    model="zai-org/GLM-4.7",
    messages=messages,
    tools=tools,
    max_tokens=4096,
    temperature=0.0,
    # extra_body={"chat_template_kwargs": {"enable_thinking": False}} # Uncomment this line to disable thinking
)
message = completion.choices[0].message
if message.tool_calls:
    messages.append(message)
    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)
        print("===== TOOL CALL =====")
        print(tool_call)
        # Simulate a weather service; each result must match its returned call ID.
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(
                    {
                        "location": args["location"],
                        "weather": "晴",
                        "temperature": "26C",
                    },
                    ensure_ascii=False,
                ),
            }
        )

    completion_2 = client.chat.completions.create(
        model="zai-org/GLM-4.7",
        messages=messages,
        tools=tools,
        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    )
    print("===== RESPONSE =====")
    print(completion_2.choices[0].message.content)
else:
    print("===== RESPONSE =====")
    print(message.content)
