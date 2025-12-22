# 测试结果

以下数据在该测试环境中测试，sglang版本为`0.4.10`，仅使用 sglang bench用于测速，可以使用更高版本的sglang 进行测速。

## 测试环境

+ 镜像版本：xllm-0.7.1
+ xllm版本：xllm/release/v0.7.0 - 1128
+ 模型 zai-org/GLM-4.6 (非FP8版本)
+ 并行策略 TP16 (8卡16芯)， 未设置其他并行策略。

## 单并发短文本测试

### 命令

```shell
python3 -m sglang.bench_serving   
 --backend sglang-oai   
 --base-url http://127.0.0.1:30000   \
 --model zai-org/GLM-4.6    \
 --dataset-name sharegpt   \
 --num-prompts 8 \   
 --random-input-len 8192 \
 --random-output-len 1024  \
 --request-rate 1 \
 --max-concurrency 1 \
 --disable-stream   
```

### 结果

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai
Traffic request rate:                    1.0
Max request concurrency:                 1
Successful requests:                     8
Benchmark duration (s):                  78.11
Total input tokens:                      33988
Total generated tokens:                  4608
Total generated tokens (retokenized):    4606
Request throughput (req/s):              0.10
Input token throughput (tok/s):          435.13
Output token throughput (tok/s):         58.99
Total token throughput (tok/s):          494.13
Concurrency:                             1.00
----------------End-to-End Latency----------------
Mean E2E Latency (ms):                   9762.78
Median E2E Latency (ms):                 10630.42
---------------Time to First Token----------------
Mean TTFT (ms):                          9762.82
Median TTFT (ms):                        10630.45
P99 TTFT (ms):                           15837.95
==================================================
```

## 单并发中长文本测试

### 命令

```shell
python3 -m sglang.bench_serving   --backend sglang-oai   
 --base-url http://127.0.0.1:30000   \
 --model zai-org/GLM-4.6    \
 --dataset-name sharegpt   \
 --num-prompts 1 \   
 --random-input-len 48000   \
 --random-output-len 1024   \
 --request-rate 1 \
 --max-concurrency 1  \
 --disable-stream
```

### 结果

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai
Traffic request rate:                    1.0
Max request concurrency:                 1
Successful requests:                     1
Benchmark duration (s):                  19.58
Total input tokens:                      33004
Total generated tokens:                  905
Total generated tokens (retokenized):    905
Request throughput (req/s):              0.05
Input token throughput (tok/s):          1685.38
Output token throughput (tok/s):         46.21
Total token throughput (tok/s):          1731.59
Concurrency:                             1.00
----------------End-to-End Latency----------------
Mean E2E Latency (ms):                   19579.00
Median E2E Latency (ms):                 19579.00
---------------Time to First Token----------------
Mean TTFT (ms):                          19579.04
Median TTFT (ms):                        19579.04
P99 TTFT (ms):                           19579.04
==================================================
```

## 高并发测试

### 命令

```shell
python3 -m sglang.bench_serving   --backend sglang-oai   
 --base-url http://127.0.0.1:30000   \
 --model zai-org/GLM-4.6    \
 --dataset-name sharegpt   \
 --num-prompts 128    \
 --disable-ignore-eos  \
 --disable-stream   \
 --request-rate 32 \
 --max-concurrency 36
```

### 结果

```
============ Serving Benchmark Result ============
Backend:                                 sglang-oai
Traffic request rate:                    32.0
Max request concurrency:                 36
Successful requests:                     128
Benchmark duration (s):                  45.36
Total input tokens:                      47692
Total generated tokens:                  24911
Total generated tokens (retokenized):    20008
Request throughput (req/s):              2.82
Input token throughput (tok/s):          1051.43
Output token throughput (tok/s):         549.19
Total token throughput (tok/s):          1600.62
Concurrency:                             26.97
----------------End-to-End Latency----------------
Mean E2E Latency (ms):                   9556.43
Median E2E Latency (ms):                 5538.18
---------------Time to First Token----------------
Mean TTFT (ms):                          9463.31
Median TTFT (ms):                        5538.20
P99 TTFT (ms):                           33160.10
==================================================
```
