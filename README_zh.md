# GLM-4.7 & GLM-4.6 & GLM-4.5

[English Version](./README.md) | [日本語版](./README_ja.md)

<div align="center">
<img src=resources/logo.svg width="15%"/>
</div>
<p align="center">
    👋 加入我们的<a href="resources/WECHAT.md" target="_blank"> 微信群 </a>或<a href="https://discord.gg/QR7SARHRxK" target="_blank"> Discord </a>社区。
    <br>
    📖 查看 GLM-4.7<a href="https://z.ai/blog/glm-4.7" target="_blank"> 技术博客 </a> ， <a href="https://arxiv.org/abs/2508.06471" target="_blank"> 技术报告(GLM-4.5) </a> 以及 <a href="https://zhipu-ai.feishu.cn/wiki/Gv3swM0Yci7w7Zke9E0crhU7n7D" target="_blank"> 智谱AI技术文档 </a>。
    <br>
    📍 在<a href="https://docs.bigmodel.cn/cn/guide/models/text/glm-4.7"> 智谱AI开放平台 </a>上使用GLM-4.7 API服务。
    <br>
    👉 一键体验 <a href="https://chat.z.ai" >GLM-4.7 </a>。
</p>

## 模型介绍

### GLM-4.7

**GLM-4.7**，您的新编程伙伴，具备以下特性：

- **核心编程能力**：与前代 GLM-4.6 相比，GLM-4.7 在多语言智能体编程和终端任务方面取得了显著提升，包括 SWE-bench（73.8%，+5.8%）、SWE-bench Multilingual（66.7%，+12.9%）和 Terminal Bench 2.0（41%，+16.5%）。GLM-4.7 还支持先思考后行动，在 Claude Code、Kilo Code、Cline 和 Roo Code 等主流智能体框架的复杂任务上有显著改进。
- **氛围编程**：GLM-4.7 在 UI 质量提升方面迈出了重要一步。它能生成更简洁、更现代的网页，并制作出布局和尺寸更精准、外观更美观的幻灯片。
- **工具使用**：GLM-4.7 在工具使用能力上取得了显著改进。在 τ²-Bench 等基准测试以及 BrowseComp 网页浏览测试中表现出明显更优的性能。
- **复杂推理**：GLM-4.7 在数学和推理能力上实现了大幅提升，在 HLE（人类终极考试）基准测试中相比 GLM-4.6 取得了（42.8%，+12.4%）的成绩。

更广泛地说，在聊天、创意写作和角色扮演等许多其他场景中，您也将看到显著的改进。

![bench](resources/bench_glm47.png)

**交错思考与保留思考**

![thinking](resources/thinking.png)

GLM-4.7 进一步增强了**交错思考**（自 GLM-4.5 引入的功能），并引入了**保留思考**和**轮次级思考**。通过在动作之间进行思考并在多轮对话中保持一致性，使复杂任务更加稳定和可控：
- **交错思考**：模型在每次响应和工具调用前进行思考，提升指令遵循能力和生成质量。
- **保留思考**：在编程智能体场景中，模型会自动在多轮对话中保留所有思考块，复用已有推理而非从头推导。这减少了信息丢失和不一致性，非常适合长周期、复杂的任务。
- **轮次级思考**：模型支持在会话中按轮次控制推理——对于轻量级请求可禁用思考以降低延迟/成本，对于复杂任务可启用思考以提高准确性和稳定性。

更多详情：https://docs.z.ai/guides/capabilities/thinking-mode

我们也提供轻量级的 30B-A3B 模型 GLM-4.7-Flash，为轻量化部署提供了一个兼顾性能与效率的新选择。

### GLM-4.6

与 GLM-4.5 相比，**GLM-4.6** 带来了几个关键改进：

- **更长的上下文窗口：** 上下文窗口从 128K 扩展到 200K tokens，使模型能够处理更复杂的智能体任务。
- **更强的代码性能：** 模型在代码基准测试中取得了更高的分数，并在实际应用中表现更佳，例如 Claude Code、Cline、Roo Code 和 Kilo Code，包括在生成视觉上更精美的前端页面方面的提升。
- **更先进的推理能力：** GLM-4.6 在推理性能上有明显提升，并在推理过程中支持工具调用，从而带来更强的整体能力。
- **更强大的智能体：** GLM-4.6 在工具使用和基于搜索的智能体方面表现更强，并能更高效地融入智能体框架。
- **更精细的写作：** 更好地符合人类在风格和可读性上的偏好，并在角色扮演场景中表现得更加自然。

我们在涵盖智能体、推理和编程的八个公共基准上对 GLM-4.6 进行了评估。结果显示，GLM-4.6 相比 GLM-4.5 有显著提升，同时在对比 **DeepSeek-V3.1-Terminus** 和 **Claude Sonnet 4** 等国内外领先模型时也展现出了竞争优势。

### GLM-4.5

**GLM-4.5** 系列模型是专为智能体设计的基础模型。GLM-4.5拥有 **3550** 亿总参数量，其中 **320** 亿活跃参数；GLM-4.5-Air 采用更紧凑的设计，拥有
 **1060** 亿总参数量，其中 **120** 亿活跃参数。GLM-4.5模型统一了推理、编码和智能体能力，以满足智能体应用的复杂需求。

GLM-4.5 和 GLM-4.5-Air 都是混合推理模型，提供两种模式：用于复杂推理和工具使用的思考模式，以及用于即时响应的非思考模式。

我们已开源了 GLM-4.5 和 GLM-4.5-Air 的基础模型、混合推理模型以及混合推理模型的FP8版本。它们采用MIT开源许可证发布，可用于商业用途和二次开发。

在我们对12项行业标准基准的全面评估中，GLM-4.5表现卓越，得分 **63.2**，在所有专有和开源模型中排名**第3**
。值得注意的是，GLM-4.5-Air在保持优异效率的同时，仍取得了 **59.8** 的竞争性成绩。

如需了解更多评估结果、展示案例和技术细节，请访问我们的 [技术报告](https://arxiv.org/abs/2508.06471)。

## 模型下载

| 模型               | 下载链接                                                                                                                                          | 模型大小      | 精度   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|------|
| GLM-4.7          | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.7)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.7)                   | 355B-A32B  | BF16      |
| GLM-4.7-FP8      | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.7-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.7-FP8)           | 355B-A32B  | FP8       |
| GLM-4.7-Flash    | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.7-Flash)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.7-Flash)       | 30B-A3B    | BF16      |
| GLM-4.6          | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.6)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.6)                   | 355B-A32B  | BF16      |
| GLM-4.6-FP8      | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.6-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.6-FP8)           | 355B-A32B  | FP8       |
| GLM-4.5          | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5)                   | 355B-A32B  | BF16      |
| GLM-4.5-Air      | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Air)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air)           | 106B-A12B  | BF16      |
| GLM-4.5-FP8      | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-FP8)           | 355B-A32B  | FP8       |
| GLM-4.5-Air-FP8  | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Air-FP8)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air-FP8)   | 106B-A12B  | FP8       |
| GLM-4.5-Base     | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Base)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Base)         | 355B-A32B  | BF16      |
| GLM-4.5-Air-Base | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-4.5-Air-Base)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-4.5-Air-Base) | 106B-A12B  | BF16      |

- GLM-4.5、GLM-4.6 和 GLM-4.7 的模型代码、工具解析器（tool parser）和推理解析器（reasoning parser）可以在以下实现中找到：[transformers](https://github.com/huggingface/transformers/tree/main/src/transformers/models/glm4_moe)、[vLLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/glm4_moe_mtp.py) 和 [SGLang](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/glm4_moe.py)。
- GLM-4.7-Flash 的模型代码可以在以下实现中找到：[transformers](https://github.com/huggingface/transformers/tree/main/src/transformers/models/glm4_moe_lite)、[vLLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/glm4_moe_lite_mtp.py) 和 [SGLang](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/glm4_moe_lite.py)。

## 系统要求

### 推理(英伟达GPU)

我们提供了"全功能"模型推理的最低和推荐配置。下表中的数据基于以下条件：

1. 所有模型都使用MTP层，并指定`--speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4`
   以确保具有竞争力的推理速度。
2. 不使用 `cpu-offload` 参数。
3. 推理批处理大小不超过 `8`。
4. 所有操作都在原生支持FP8推理的设备上执行，确保权重和缓存都采用FP8格式。
5. 服务器内存必须超过 `1T` 以确保正常的模型加载和运行。

模型可在下表配置下运行：

| 模型            | 精度   | GPU类型和数量   |
|---------------|------|------------|
| GLM-4.5       | BF16 | H100 x 16  |
| GLM-4.5       | FP8  | H100 x 8   |
| GLM-4.5-Air   | BF16 | H100 x 4   |
| GLM-4.5-Air   | FP8  | H100 x 2   |
| GLM-4.7-Flash | BF16 | H100 x 1   |

在下表配置下，模型可以充分利用其全部上下文长度：

| 模型            | 精度   | GPU类型和数量   |
|---------------|------|------------|
| GLM-4.5       | BF16 | H100 x 32  |
| GLM-4.5       | FP8  | H100 x 16  |
| GLM-4.5-Air   | BF16 | H100 x 8   |
| GLM-4.5-Air   | FP8  | H100 x 4   |
| GLM-4.7-Flash | BF16 | H100 x 2   |

### 其他设备

- 使用 [xLLM](https://github.com/jd-opensource/xllm) 在 Ascend A3 设备上进行快速推理，请查看 [Ascend NPU 部署文档](example/Ascend_NPU/README_zh.md)。
- 使用 AMD 的 GPU 进行推理，请查看 [AMD GPU 部署文档](example/AMD_GPU/README_zh.md)。

### 微调

使用 [Llama Factory](https://github.com/hiyouga/LLaMA-Factory) 框架，代码可在下表配置下运行：

| 模型          | GPU类型和数量  | 策略   | 批处理大小（每GPU） |
|-------------|-----------|------|-------------|
| GLM-4.5     | H100 x 16 | Lora | 1           |
| GLM-4.5-Air | H100 x 4  | Lora | 1           |

使用 [Swift](https://github.com/modelscope/ms-swift) 框架，代码可在下表配置下运行：

| 模型          | GPU类型和数量          | 策略   | 批处理大小（每GPU） |
|-------------|-------------------|------|-------------|
| GLM-4.5     | H20 (96GiB) x 16  | Lora | 1           |
| GLM-4.5-Air | H20 (96GiB) x 4   | Lora | 1           |
| GLM-4.5     | H20 (96GiB) x 128 | SFT  | 1           |
| GLM-4.5-Air | H20 (96GiB) x 32  | SFT  | 1           |
| GLM-4.5     | H20 (96GiB) x 128 | RL   | 1           |
| GLM-4.5-Air | H20 (96GiB) x 32  | RL   | 1           |

## 快速开始

vLLM 和 SGLang 仅在其主分支上支持 GLM-4.7-Flash。您可以使用它们的官方 Docker 镜像进行推理。

- vLLM

    ```shell
        docker pull vllm/vllm-openai:nightly 
    ```
    或使用 pip 安装（必须使用 pypi.org 作为索引 URL）：
    ```shell
        pip install -U vllm --pre --index-url https://pypi.org/simple --extra-index-url https://wheels.vllm.ai/nightly
    ```

- SGLang

    ```shell
        docker pull lmsysorg/sglang:dev
    ```
    在 Docker 容器中运行：
    ```shell
        pip install git+https://github.com/huggingface/transformers.git@76732b4e7120808ff989edbd16401f61fa6a0afa
    ```

    或从源代码使用 pip 安装 sglang。

对于 GLM-4.7、GLM-4.6 和 GLM-4.5，您可以按照 `requirements.txt` 中的配置进行操作。

### transformers

请参考 `inference` 文件夹中的 `trans_infer_cli.py` 代码。

### vLLM

```shell
vllm serve zai-org/GLM-4.7-FP8 \
     --tensor-parallel-size 4 \
     --speculative-config.method mtp \
     --speculative-config.num_speculative_tokens 1 \
     --tool-call-parser glm47 \
     --reasoning-parser glm45 \
     --enable-auto-tool-choice \
     --served-model-name glm-4.7-fp8
```

### SGLang

```shell
python3 -m sglang.launch_server \
  --model-path zai-org/GLM-4.7-FP8 \
  --tp-size 8 \
  --tool-call-parser glm47  \
  --reasoning-parser glm45 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.8 \
  --served-model-name glm-4.7-fp8 \
  --host 0.0.0.0 \
  --port 8000
```

- PD 分离

以下是使用单机多卡器实现PD分离的简单办法，其中P和D各使用4张GPU。

```shell
python -m sglang.launch_server --model-path zai-org/GLM-4.5-Air  --disaggregation-mode prefill --disaggregation-ib-device mlx5_0 --tp-size 4
python -m sglang.launch_server --model-path zai-org/GLM-4.5-Air  --disaggregation-mode decode --port 30001 --disaggregation-ib-device mlx5_0 --tp-size 4 --base-gpu-id 4                                                                                                                                                        
python -m sglang_router.launch_router --pd-disaggregation --prefill http://127.0.0.1:30000 --decode http://127.0.0.1:30001 --host 0.0.0.0 --port 8000
```

### 参数说明

- 对于 GLM-4.7，在 `vLLM` 和 `SGLang` 两种方法中，`--tool-call-parser` 都应设置为 `glm47`。
- 对于 GLM-4.7 的智能体任务，请通过添加以下配置开启[保留思考模式](https://docs.z.ai/guides/capabilities/thinking-mode)（仅 sglang 支持）：
  
  ```
    "chat_template_kwargs": {
        "enable_thinking": true,
        "clear_thinking": false
    }
    ```
  
- 使用`vLLM`和`SGLang`时，发送请求时默认启用思考模式。如果要禁用思考开关，需要添加
`extra_body={"chat_template_kwargs": {"enable_thinking": False}}`参数。
- 两者都支持工具调用。请使用OpenAI风格的工具描述格式进行调用。
- 具体代码请参考`inference`文件夹中的`api_request.py`。

### 验证

- 有关工具集成推理，请参阅 [文档](resources/glm_4.6_tir_guide.md)。

- 用于搜索基准测试，我们在 **thinking 模式** 下为搜索工具调用设计了一种特定格式，以支持搜索代理。详细模板请参阅 [此处](resources/trajectory_search.json)。

## 引用

如果您发现我们的工作对您的研究有帮助，请考虑引用以下论文：

```bibtex
@misc{5team2025glm45agenticreasoningcoding,
      title={GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models}, 
      author={GLM Team and Aohan Zeng and Xin Lv and Qinkai Zheng and Zhenyu Hou and Bin Chen and Chengxing Xie and Cunxiang Wang and Da Yin and Hao Zeng and Jiajie Zhang and Kedong Wang and Lucen Zhong and Mingdao Liu and Rui Lu and Shulin Cao and Xiaohan Zhang and Xuancheng Huang and Yao Wei and Yean Cheng and Yifan An and Yilin Niu and Yuanhao Wen and Yushi Bai and Zhengxiao Du and Zihan Wang and Zilin Zhu and Bohan Zhang and Bosi Wen and Bowen Wu and Bowen Xu and Can Huang and Casey Zhao and Changpeng Cai and Chao Yu and Chen Li and Chendi Ge and Chenghua Huang and Chenhui Zhang and Chenxi Xu and Chenzheng Zhu and Chuang Li and Congfeng Yin and Daoyan Lin and Dayong Yang and Dazhi Jiang and Ding Ai and Erle Zhu and Fei Wang and Gengzheng Pan and Guo Wang and Hailong Sun and Haitao Li and Haiyang Li and Haiyi Hu and Hanyu Zhang and Hao Peng and Hao Tai and Haoke Zhang and Haoran Wang and Haoyu Yang and He Liu and He Zhao and Hongwei Liu and Hongxi Yan and Huan Liu and Huilong Chen and Ji Li and Jiajing Zhao and Jiamin Ren and Jian Jiao and Jiani Zhao and Jianyang Yan and Jiaqi Wang and Jiayi Gui and Jiayue Zhao and Jie Liu and Jijie Li and Jing Li and Jing Lu and Jingsen Wang and Jingwei Yuan and Jingxuan Li and Jingzhao Du and Jinhua Du and Jinxin Liu and Junkai Zhi and Junli Gao and Ke Wang and Lekang Yang and Liang Xu and Lin Fan and Lindong Wu and Lintao Ding and Lu Wang and Man Zhang and Minghao Li and Minghuan Xu and Mingming Zhao and Mingshu Zhai and Pengfan Du and Qian Dong and Shangde Lei and Shangqing Tu and Shangtong Yang and Shaoyou Lu and Shijie Li and Shuang Li and Shuang-Li and Shuxun Yang and Sibo Yi and Tianshu Yu and Wei Tian and Weihan Wang and Wenbo Yu and Weng Lam Tam and Wenjie Liang and Wentao Liu and Xiao Wang and Xiaohan Jia and Xiaotao Gu and Xiaoying Ling and Xin Wang and Xing Fan and Xingru Pan and Xinyuan Zhang and Xinze Zhang and Xiuqing Fu and Xunkai Zhang and Yabo Xu and Yandong Wu and Yida Lu and Yidong Wang and Yilin Zhou and Yiming Pan and Ying Zhang and Yingli Wang and Yingru Li and Yinpei Su and Yipeng Geng and Yitong Zhu and Yongkun Yang and Yuhang Li and Yuhao Wu and Yujiang Li and Yunan Liu and Yunqing Wang and Yuntao Li and Yuxuan Zhang and Zezhen Liu and Zhen Yang and Zhengda Zhou and Zhongpei Qiao and Zhuoer Feng and Zhuorui Liu and Zichen Zhang and Zihan Wang and Zijun Yao and Zikang Wang and Ziqiang Liu and Ziwei Chai and Zixuan Li and Zuodong Zhao and Wenguang Chen and Jidong Zhai and Bin Xu and Minlie Huang and Hongning Wang and Juanzi Li and Yuxiao Dong and Jie Tang},
      year={2025},
      eprint={2508.06471},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.06471}, 
}
```
