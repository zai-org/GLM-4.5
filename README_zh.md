# GLM-4.5

[Read this in English.](./README.md)

<p align="center">
    👋 加入我们的 <a href="resources/WECHAT.md" target="_blank">微信</a> 和 <a href="https://discord.com/invite/8cnQKdAprg" target="_blank">Discord</a> 社区。
    <br>
    📖 查看 GLM-4.5 <a href="" target="_blank">技术博客</a> 。
    <br>
    📍 在 <a href="https://www.bigmodel.cn/dev/api/visual-reasoning-model/GLM-4.5">智谱大模型开放平台</a> 使用 GLM-4.5 的API服务。
</p>

## 模型介绍

## 下载模型

| 模型               | 下载地址                                                                                                                                       | 权重大小      | 精度   |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------|------|
| GLM-4.5          | [🤗Hugging Face](https://huggingface.co/THUDM/GLM-4.5)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5)                   | 355B-A32B | BF16 |
| GLM-4.5-Air      | [🤗Hugging Face](https://huggingface.co/THUDM/GLM-4.5-Air)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air)           | 106B-A12B | BF16 |
| GLM-4.5-FP8      | [🤗Hugging Face](https://huggingface.co/THUDM/GLM-4.5-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-FP8)           | 106B-A12B | FP8  |
| GLM-4.5-Air-FP8  | [🤗Hugging Face](https://huggingface.co/THUDM/GLM-4.5-Air-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air-FP8)   | 106B-A12B | FP8  |
| GLM-4.5-Base     | [🤗Hugging Face](https://huggingface.co/THUDM/GLM-4.5-Base)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Base)         | 355B-A32B | BF16 |
| GLM-4.5-Air-Base | [🤗Hugging Face](https://huggingface.co/THUDM/GLM-4.5-Air-Base)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air-Base) | 106B-A12B | BF16 |

模型算法代码可以查看 [transformers](https://github.com/huggingface/transformers/tree/main/src/transformers/models/glm4_moe)
的完整实现。

## 运行要求

+ 以下数据均使用 `BF16`精度微调和推理。
+ 相关配置信息：
    + 操作系统: `Ubuntu 22.04`
    + CUDA 版本: `12.8`
    + Python 版本: `3.10.12`
    + 内存: `2TB`

数据仅供参考, 具体性能提升以开发者部署为准。

### 推理 (SGLang)

| 模型          | 设备          | 数量 | 输出速度 |
|-------------|-------------|----|------|
| GLM-4.5     | NVIDIA H200 | 8  |      |
| GLM-4.5-Air | NVIDIA H200 | 4  |      |

### 微调 (LLaMA-Factory)

| 模型          | 设备(集群)      | 策略         | 需要卡数 | 批大小 (per GPUs) |
|-------------|-------------|------------|------|----------------|
| GLM-4.5     | NVIDIA H100 | Lora ZERO3 | 16   | 1              |
| GLM-4.5-Air | NVIDIA H100 | Lora ZERO3 | 4    | 1              |

### 微调 (SWIFT)

| 模型          | 设备(集群)      | 策略   | 需要卡数 | 批大小 (per GPUs) |
|-------------|-------------|------|------|----------------|
| GLM-4.5     | NVIDIA H100 | Lora | 16   | 1              |
| GLM-4.5-Air | NVIDIA H100 | Lora | 4    | 1              |
| GLM-4.5     | NVIDIA H100 | SFT  | 16   | 1              |
| GLM-4.5-Air | NVIDIA H100 | SFT  | 4    | 1              |
| GLM-4.5     | NVIDIA H100 | RL   | 16   | 1              |
| GLM-4.5-Air | NVIDIA H100 | RL   | 4    | 1              |

## 快速上手

请按照 `requirements.txt` 中的依赖安装相关包。

```shell
pip install -r requirements.txt
```

### transformers

请查看 `inference` 文件夹中的 `trans_infer_cli.py`代码。

### vLLM

+ BF16

```shell
vllm serve /mnt/GLM-4.5-FP8-0724 \
    --tensor-parallel-size 8 \
    --tool-call-parser glm45 \
    --reasoning-parser glm45 \
    --enable-auto-tool-choice \
    --served-model-name glm-4.5-air
```

### SGLang

+ BF16

```shell
python3 -m sglang.launch_server \
  --model-path THUDM/GLM-4.5-Air \
  --tp-size 8 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.7 \
  --served-model-name glm-4.5-air
```

+ FP8

```shell
python3 -m sglang.launch_server \
  --model-path THUDM/GLM-4.5-Air-FP8 \
  --tp-size 4 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45  \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3  \
  --speculative-eagle-topk 1  \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.7 \
  --disable-shared-experts-fusion \
  --served-model-name glm-4.5-air-fp8
```

### 请求

+ 使用`vLLM`和`SGLang`时，发送请求时候默认思考，如果希望关闭思考开关，则需要增加
  `extra_body={"chat_template_kwargs": {"enable_thinking": False}}` 参数。
+ 均支持工具调用。请使用 OpenAI 类格式工具描述调用。
+ 具体代码请查看`inference`文件夹中的`api_request.py`。

## 引用论文

如果您使用了本模型，请引用以下论文：

```bibtex

```
