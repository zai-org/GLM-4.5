## AMD GPU Installation and Testing Guide 
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
