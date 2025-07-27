# Setting up Claude Code Service with SGLang + GLM-4.5 Model

[中文阅读](./README_zh.md)

## Installation

You need to have a local computer device for programming and a server for running the `GLM-4.5` model.

### Local Device

Ensure you have installed [Claude Code](https://github.com/anthropics/claude-code)
and [Claude Code Router](https://github.com/musistudio/claude-code-router).

```
npm install -g @anthropic-ai/claude-code
npm install -g @musistudio/claude-code-router
```

### Server

Ensure you have installed `sglang` on your server.

```shell
pip install sglang
```

And start the model service with the following command:

```shell
python3 -m sglang.launch_server \
  --model-path zai-org/GLM-4.5 \
  --tp-size 16 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.7 \
  --served-model-name glm-4.5 \
  --port 8000 \
  --host 0.0.0.0 # Or your server's internal/public IP address
```

When successful, you will see output similar to the following:

```
[2025-07-26 16:09:07] INFO:     Started server process [80269]
[2025-07-26 16:09:07] INFO:     Waiting for application startup.
[2025-07-26 16:09:07] INFO:     Application startup complete.
[2025-07-26 16:09:07] INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
[2025-07-26 16:09:08] INFO:     127.0.0.1:57722 - "GET /get_model_info HTTP/1.1" 200 OK
[2025-07-26 16:09:11] INFO:     127.0.0.1:57732 - "POST /generate HTTP/1.1" 200 OK
[2025-07-26 16:09:11] The server is fired up and ready to roll!
```

Please ensure your server's IP can be accessed from the device where Claude Code and Claude Code Router are installed.

## Configuration

1. Modify the `api_base_url` in `config.example.json` to your server's accessible address.
2. Rename it to `config.json`
3. Copy it to `~/.claude-code-router/config.json`.
4. Execute the `ccr restart` command in the command line. You should see the following output:
  
    ```
    Service was not running or failed to stop.
    Starting claude code router service...
    ✅ Service started successfully in the background.
    ```

## Running

Execute the following command:

```
ccr code
```

It should looks like:

```
zr@MacBook GLM-4.5 % ccr code
Service not running, starting service...
╭───────────────────────────────────────────────────╮
│ ✻ Welcome to Claude Code!                         │
│                                                   │
│   /help for help, /status for your current setup  │
│                                                   │
│   cwd: /Users/zr/Code/GLM-4.5                     │
│                                                   │
│   ─────────────────────────────────────────────── │
│                                                   │
│   Overrides (via env):                            │
│                                                   │
│   • API timeout: 600000ms                         │
│   • API Base URL: http://127.0.0.1:3456           │
╰───────────────────────────────────────────────────╯

 ※ Tip: Press Esc twice to edit your previous messages


> how can I run GLM-4.5 in transformers

⏺ I'll help you understand how to run GLM-4.5 in transformers. Let me first explore the codebase to see what's available.

⏺ List(.)
  ⎿  Listed 21 paths (ctrl+r to expand)

⏺ Read(README.md)
  ⎿  Read 4 lines (ctrl+r to expand)

⏺ Read(inference/trans_infer_cli.py)
  ⎿  Read 29 lines (ctrl+r to expand)

⏺ Read(requirements.txt)
  ⎿  Read 5 lines (ctrl+r to expand)

⏺ You can run GLM-4.5 in transformers using the example script in inference/trans_infer_cli.py. Here's the basic approach:

  from transformers import AutoModelForCausalLM, AutoTokenizer
  import torch

  MODEL_PATH = "zai-org/GLM-4.5"
  tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
  model = AutoModelForCausalLM.from_pretrained(
      MODEL_PATH,
      torch_dtype=torch.bfloat16,
      device_map="auto"
  )

  Then use the tokenizer's chat template for inference.

╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ >                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ? for shortcuts
```
