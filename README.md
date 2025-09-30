# GLM-4.6 & GLM-4.5

[中文阅读](./README_zh.md) | [日本語版](./README_ja.md)

<div align="center">
<img src=resources/logo.svg width="15%"/>
</div>
<p align="center">
    👋 Join our <a href="resources/WECHAT.md" target="_blank">WeChat</a> or <a href="https://discord.gg/QR7SARHRxK" target="_blank">Discord</a> community.
    <br>
    📖 Check out the GLM-4.6 <a href="https://z.ai/blog/glm-4.6" target="_blank">technical blog</a>, <a href="https://arxiv.org/abs/2508.06471" target="_blank">technical report(GLM-4.5)</a>, and <a href="https://zhipu-ai.feishu.cn/wiki/Gv3swM0Yci7w7Zke9E0crhU7n7D" target="_blank">Zhipu AI technical documentation</a>.
    <br>
    📍 Use GLM-4.6 API services on <a href="https://docs.z.ai/guides/llm/glm-4.6">Z.ai API Platform</a>.
    <br>
    👉 One click to <a href="https://chat.z.ai">GLM-4.6</a>.
</p>

## Model Introduction

### GLM-4.6

Compared with GLM-4.5, **GLM-4.6**  brings several key improvements:

* **Longer context window:** The context window has been expanded from 128K to 200K tokens, enabling the model to handle more complex agentic tasks.
* **Superior coding performance:** The model achieves higher scores on code benchmarks and demonstrates better real-world performance in applications such as Claude Code、Cline、Roo Code and Kilo Code, including improvements in generating visually polished front-end pages.
* **Advanced reasoning:** GLM-4.6 shows a clear improvement in reasoning performance and supports tool use during inference, leading to stronger overall capability.
* **More capable agents:** GLM-4.6 exhibits stronger performance in tool using and search-based agents, and integrates more effectively within agent frameworks.
* **Refined writing:** Better aligns with human preferences in style and readability, and performs more naturally in role-playing scenarios.

We evaluated GLM-4.6 across eight public benchmarks covering agents, reasoning, and coding. Results show clear gains over GLM-4.5, with GLM-4.6 also holding competitive advantages over leading domestic and international models such as **DeepSeek-V3.1-Terminus** and **Claude Sonnet 4**.

![bench](resources/bench_glm46.png)

### GLM-4.5

The **GLM-4.5** series models are foundation models designed for intelligent agents. GLM-4.5 has **355** billion total
parameters with **32** billion active parameters, while GLM-4.5-Air adopts a more compact design with **106** billion
total parameters and **12** billion active parameters. GLM-4.5 models unify reasoning, coding, and intelligent agent
capabilities to meet the complex demands of intelligent agent applications.

Both GLM-4.5 and GLM-4.5-Air are hybrid reasoning models that provide two modes: thinking mode for complex reasoning and
tool usage, and non-thinking mode for immediate responses.

We have open-sourced the base models, hybrid reasoning models, and FP8 versions of the hybrid reasoning models for both
GLM-4.5 and GLM-4.5-Air. They are released under the MIT open-source license and can be used commercially and for
secondary development.

As demonstrated in our comprehensive evaluation across 12 industry-standard benchmarks, GLM-4.5 achieves exceptional
performance with a score of **63.2**, in the **3rd** place among all the proprietary and open-source models. Notably,
GLM-4.5-Air delivers competitive results at **59.8** while maintaining superior efficiency.

![bench](resources/bench.png)

For more eval results, show cases, and technical details, please visit
our [technical report](https://arxiv.org/abs/2508.06471) or [technical blog](https://z.ai/blog/glm-4.5).

The model code, tool parser and reasoning parser can be found in the implementation
of [transformers](https://github.com/huggingface/transformers/tree/main/src/transformers/models/glm4_moe), [vLLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/glm4_moe_mtp.py)
and [SGLang](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/glm4_moe.py).

## Model Downloads

You can directly experience the model on [Hugging Face](https://huggingface.co/spaces/zai-org/GLM-4.5-Space)
or [ModelScope](https://modelscope.cn/studios/ZhipuAI/GLM-4.5-Demo) or download the model by following the links below.

| Model            | Download Links                                                                                                                                | Model Size | Precision |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------|
| GLM-4.6          | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.6)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.6)                   | 355B-A32B  | BF16      |
| GLM-4.5          | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5)                   | 355B-A32B  | BF16      |
| GLM-4.5-Air      | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Air)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air)           | 106B-A12B  | BF16      |
| GLM-4.5-FP8      | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-FP8)           | 355B-A32B  | FP8       |
| GLM-4.5-Air-FP8  | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Air-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air-FP8)   | 106B-A12B  | FP8       |
| GLM-4.5-Base     | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Base)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Base)         | 355B-A32B  | BF16      |
| GLM-4.5-Air-Base | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Air-Base)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air-Base) | 106B-A12B  | BF16      |

## System Requirements

### Inference

We provide minimum and recommended configurations for "full-featured" model inference. The data in the table below is
based on the following conditions:

1. All models use MTP layers and specify
   `--speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4` to ensure competitive
   inference speed.
2. The `cpu-offload` parameter is not used.
3. Inference batch size does not exceed `8`.
4. All are executed on devices that natively support FP8 inference, ensuring both weights and cache are in FP8 format.
5. Server memory must exceed `1T` to ensure normal model loading and operation.

The models can run under the configurations in the table below:

| Model       | Precision | GPU Type and Count   | Test Framework |
|-------------|-----------|----------------------|----------------|
| GLM-4.5     | BF16      | H100 x 16 / H200 x 8 | sglang         |
| GLM-4.5     | FP8       | H100 x 8 / H200 x 4  | sglang         |
| GLM-4.5-Air | BF16      | H100 x 4 / H200 x 2  | sglang         |
| GLM-4.5-Air | FP8       | H100 x 2 / H200 x 1  | sglang         |

Under the configurations in the table below, the models can utilize their full 128K context length:

| Model       | Precision | GPU Type and Count    | Test Framework |
|-------------|-----------|-----------------------|----------------|
| GLM-4.5     | BF16      | H100 x 32 / H200 x 16 | sglang         |
| GLM-4.5     | FP8       | H100 x 16 / H200 x 8  | sglang         |
| GLM-4.5-Air | BF16      | H100 x 8 / H200 x 4   | sglang         |
| GLM-4.5-Air | FP8       | H100 x 4 / H200 x 2   | sglang         |

if you are using AMD GPUs, Check [here](example/AMD_GPU/README.md) for AMD GPU deployment documentation.

### Fine-tuning

The code can run under the configurations in the table below
using [Llama Factory](https://github.com/hiyouga/LLaMA-Factory):

| Model       | GPU Type and Count | Strategy | Batch Size (per GPU) |
|-------------|--------------------|----------|----------------------|
| GLM-4.5     | H100 x 16          | Lora     | 1                    |
| GLM-4.5-Air | H100 x 4           | Lora     | 1                    |

The code can run under the configurations in the table below using [Swift](https://github.com/modelscope/ms-swift):

| Model       | GPU Type and Count | Strategy | Batch Size (per GPU) |
|-------------|--------------------|----------|----------------------|
| GLM-4.5     | H20 (96GiB) x 16   | Lora     | 1                    |
| GLM-4.5-Air | H20 (96GiB) x 4    | Lora     | 1                    |
| GLM-4.5     | H20 (96GiB) x 128  | SFT      | 1                    |
| GLM-4.5-Air | H20 (96GiB) x 32   | SFT      | 1                    |
| GLM-4.5     | H20 (96GiB) x 128  | RL       | 1                    |
| GLM-4.5-Air | H20 (96GiB) x 32   | RL       | 1                    |

## Quick Start

**Both GLM-4.5 and GLM-4.6 use the same inference method.**

First, install the required packages according to `requirements.txt`.

```shell
pip install -r requirements.txt
```

### transformers

Please refer to the `trans_infer_cli.py` code in the `inference` folder.

### vLLM

+ Both BF16 and FP8 can be started with the following code:

```shell
vllm serve zai-org/GLM-4.5-Air \
    --tensor-parallel-size 8 \
    --tool-call-parser glm45 \
    --reasoning-parser glm45 \
    --enable-auto-tool-choice \
    --served-model-name glm-4.5-air
```

If you're using 8x H100 GPUs and encounter insufficient memory when running the GLM-4.5 / GLM-4.6 model, you'll need
`--cpu-offload-gb 16` (only applicable to vLLM).

If you encounter `flash infer` issues, use `VLLM_ATTENTION_BACKEND=XFORMERS` as a temporary replacement. You can also
specify `TORCH_CUDA_ARCH_LIST='9.0+PTX'` to use `flash infer` (different GPUs have different TORCH_CUDA_ARCH_LIST
values, please check accordingly).

### SGLang

+ BF16

```shell
python3 -m sglang.launch_server \
  --model-path zai-org/GLM-4.5-Air \
  --tp-size 8 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.7 \
  --served-model-name glm-4.5-air \
  --host 0.0.0.0 \
  --port 8000
```

+ FP8

```shell
python3 -m sglang.launch_server \
  --model-path zai-org/GLM-4.5-Air-FP8 \
  --tp-size 4 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45  \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3  \
  --speculative-eagle-topk 1  \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.7 \
  --disable-shared-experts-fusion \
  --served-model-name glm-4.5-air-fp8 \
  --host 0.0.0.0 \
  --port 8000
```

+ PD-Disaggregation

The following is a simple method to implement PD-Disaggregation using a single machine with multiple GPUs, P and D each use 4 GPUs.

```shell
python -m sglang.launch_server --model-path zai-org/GLM-4.5-Air  --disaggregation-mode prefill --disaggregation-ib-device mlx5_0 --tp-size 4
python -m sglang.launch_server --model-path zai-org/GLM-4.5-Air  --disaggregation-mode decode --port 30001 --disaggregation-ib-device mlx5_0 --tp-size 4 --base-gpu-id 4                                                                                                                                                        
python -m sglang_router.launch_router --pd-disaggregation --prefill http://127.0.0.1:30000 --decode http://127.0.0.1:30001 --host 0.0.0.0 --port 8000
```

### Request Parameter Instructions

+ When using `vLLM` and `SGLang`, thinking mode is enabled by default when sending requests. If you want to disable the
  thinking switch, you need to add the `extra_body={"chat_template_kwargs": {"enable_thinking": False}}` parameter.
+ Both support tool calling. Please use OpenAI-style tool description format for calls.
+ For specific code, please refer to `api_request.py` in the `inference` folder.

### Evaluation 

+ For tool-integrated reasoning, please refer to [this doc](resources/glm_4.6_tir_guide.md).
+ For search benchmark, we design a specific format for searching toolcall in thinking mode to support search agent, please refer to [this](resources/trajectory_search.json). for the detailed template.
