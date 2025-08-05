# GLM-4.5

[中文阅读](./README_zh.md)

<div align="center">
<img src=resources/logo.svg width="15%"/>
</div>
<p align="center">
    👋 Join our <a href="resources/WECHAT.md" target="_blank">WeChat</a> or <a href="https://discord.gg/QR7SARHRxK" target="_blank">Discord</a> community.
    <br>
    📖 Check out the GLM-4.5 <a href="https://z.ai/blog/glm-4.5" target="_blank">technical blog</a>.
    <br>
    📍 Use GLM-4.5 API services on <a href="https://docs.z.ai/guides/llm/glm-4.5">Z.ai API Platform (Global)</a> or <br> <a href="https://docs.bigmodel.cn/cn/guide/models/text/glm-4.5">Zhipu AI Open Platform (Mainland China)</a>.
    <br>
    👉 One click to <a href="https://chat.z.ai">GLM-4.5</a>.
</p>

## Model Introduction

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
our [technical blog](https://z.ai/blog/glm-4.5). The technical report will be released soon.

The model code, tool parser and reasoning parser can be found in the implementation
of [transformers](https://github.com/huggingface/transformers/tree/main/src/transformers/models/glm4_moe), [vLLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/glm4_moe_mtp.py)
and [SGLang](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/glm4_moe.py).

## Model Downloads

You can directly experience the model on [Hugging Face](https://huggingface.co/spaces/zai-org/GLM-4.5-Space)
or [ModelScope](https://modelscope.cn/studios/ZhipuAI/GLM-4.5-Demo) or download the model by following the links below.

| Model            | Download Links                                                                                                                                | Model Size | Precision |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------|
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


## Quick Start

### transformers

Please refer to the `trans_infer_cli.py` code in the `inference` folder.

### vLLM
### Please follow the steps here to install and run GLM models on AMD MI300X GPU.
### Step By Step Guide
#### Step 1
Launch the Rocm-vllm docker: 
```shell
docker run -it --rm \
  --cap-add=SYS_PTRACE \
  -e SHELL=/bin/bash \
  --network=host \
  --security-opt seccomp=unconfined \
  --device=/dev/kfd \
  --device=/dev/dri \
  -v /:/workspace \
  --group-add video \
  --ipc=host \
  --name vllm_GLM \
rocm/vllm-dev:nightly
```
#### Step 2
  Huggingface login
```shell
   huggingface-cli login 
```   
  Install pre-requisites:
```shell
  pip uninstall vllm 
  pip install --upgrade pip
  pip install -r rocm-requirements.txt
  git clone https://github.com/vllm-project/vllm.git
  cd vllm 
  export PYTORCH_ROCM_ARCH="gfx942"
  python3 setup.py develop
```
### Please wait until the compilation completed.
```shell
-- Found Torch: /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch.so
-- The HIP compiler identification is Clang 19.0.0
-- Detecting HIP compiler ABI info
-- Detecting HIP compiler ABI info - done
-- Check for working HIP compiler: /opt/rocm/lib/llvm/bin/clang++ - skipped
-- Detecting HIP compile features
-- Detecting HIP compile features - done
-- HIP supported arches: gfx906;gfx908;gfx90a;gfx942;gfx950;gfx1030;gfx1100;gfx1101;gfx1200;gfx1201
-- FetchContent base directory: /app/GLM-4.5/vllm/.deps
-- Enabling C extension.
-- Enabling moe extension.
-- Configuring done (19.7s)
-- Generating done (0.0s)
-- Build files have been written to: /app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312
[1/35] Running hipify on _C extension source files.
/app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/mamba/mamba_ssm/selective_scan.h -> /app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/mamba/mamba_ssm/selective_scan_hip.h [ok]
/app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/mamba/mamba_ssm/static_switch.h -> /app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/mamba/mamba_ssm/static_switch.h [skipped, no changes]
/app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/mamba/mamba_ssm/selective_scan_fwd.cu -> /app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/mamba/mamba_ssm/selective_scan_fwd.hip [ok]
/app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/cuda_utils.h -> /app/GLM-4.5/vllm/build/temp.linux-x86_64-cpython-312/csrc/hip_utils.h [ok]
...
...
...
Using /usr/local/lib/python3.12/dist-packages
Finished processing dependencies for vllm==0.10.1.dev343+g54de71d0d.rocm641
```
#### Step 3
Run the vllm online serving
Sample Command
```shell
VLLM_USE_V1=1 vllm serve zai-org/GLM-4.5 --tensor-parallel-size 8 --gpu-memory-utilization 0.95 --disable-log-requests --no-enable-prefix-caching --trust-remote-code 
```
