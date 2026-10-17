# 使用 SGLang + GLM-4.5 模型搭建Claude Code服务

[Read this in English.](./README.md)

## 安装

你需要拥有一台本地的电脑设备，这是你的编程设备，和一台服务器用于运行`GLM-4.5`模型。

### 本地设备

确保您已安装 [Claude Code](https://github.com/anthropics/claude-code)
和 [Claude Code Router](https://github.com/musistudio/claude-code-router)。

```
npm install -g @anthropic-ai/claude-code
npm install -g @musistudio/claude-code-router
```

### 服务器

确保你再服务器上已安装`sglang`。

```shell
pip install sglang
```

并使用如下命令启动模型服务:

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
  --host 0.0.0.0 # 或者你服务器的内网/公网IP地址
```

运行成功时， 你将会看到类似如下输出:

```
[2025-07-26 16:09:07] INFO:     Started server process [80269]
[2025-07-26 16:09:07] INFO:     Waiting for application startup.
[2025-07-26 16:09:07] INFO:     Application startup complete.
[2025-07-26 16:09:07] INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
[2025-07-26 16:09:08] INFO:     127.0.0.1:57722 - "GET /get_model_info HTTP/1.1" 200 OK
[2025-07-26 16:09:08 TP0] Prefill batch. #new-seq: 1, #new-token: 6, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0, 
[2025-07-26 16:09:11] INFO:     127.0.0.1:57732 - "POST /generate HTTP/1.1" 200 OK
[2025-07-26 16:09:11] The server is fired up and ready to roll!
```

请确保你的服务器的IP能被你 Claude Code 和 Claude Code Router 安装的设备上访问。

## 配置

1. 将 `config.example.json` 中的 `api_base_url` 修改为服务器的可访问地址。
2. 重命名为 `config.json`
3. 复制到 `~/.claude-code-router/config.json` 中。
4. 再命令行执行`ccr restart` 命令。得到如下输出
  
```
Service was not running or failed to stop.
Starting claude code router service...
✅ Service started successfully in the background.
```

## 运行

执行以下命令:

```
ccr code
```

即可正常运行，效果如下:

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

## 可选：使用 Parallel Search MCP 进行网络研究

[Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) 为
Claude Code 提供网络搜索和网页抓取功能。匿名端点无需账号或 API 密钥，搜索使用
Fast 模式，并有免费额度的速率限制。

完成上述 GLM 配置并确认可以正常使用后，在本地设备上进入运行 `ccr code`
时使用的同一个项目目录，执行：

```shell
claude mcp add --transport http --scope local parallel-search https://search.parallel.ai/mcp \
  --header "User-Agent: GLM-4.5-Claude-Code"
claude mcp get parallel-search
```

该命令仅为当前用户在当前项目中注册服务器，保留已有模型路由和其他 MCP 服务器，
无需修改 `~/.claude-code-router/config.json`。搜索查询和抓取的 URL 会发送给 Parallel。

重新启动 `ccr code`，然后在 Claude Code 中运行 `/mcp`，确认 `parallel-search`
已连接并提供 `web_search` 和 `web_fetch`。出现提示时批准工具调用。例如，可以输入：

```text
使用 parallel-search 查找当前 SGLang 官方文档中关于部署 GLM-4.5 的说明。
抓取最相关的官方页面，总结工具调用的配置方法，并引用来源 URL。不要修改任何文件。
```

如需移除此可选服务器，请在同一个项目目录中执行：

```shell
claude mcp remove --scope local parallel-search
```

有关作用域和连接问题的排查方法，请参阅
[Claude Code MCP 指南](https://code.claude.com/docs/en/mcp)。
