#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_gpu.py —— PyTorch + CUDA 环境一键自检
用法:
    python check_gpu.py
退出码: 0 = 全部通过; 1 = 存在失败项
"""
import sys

PASS, FAIL = "[PASS]", "[FAIL]"


def main() -> int:
    print("=" * 60)
    print(" PyTorch + CUDA 环境自检")
    print("=" * 60)
    failed = False

    # 1. Python 版本
    pyver = sys.version.split()[0]
    print(f"{PASS} Python 版本 : {pyver}")
    major, minor = int(pyver.split(".")[0]), int(pyver.split(".")[1])
    if (major, minor) >= (3, 14):
        print(f"{FAIL} Python >= 3.14 对 PyTorch 生态支持不稳定，建议 conda 建立 python=3.11 环境")
        failed = True

    # 2. 导入 torch
    try:
        import torch
    except ImportError:
        print(f"{FAIL} 未安装 torch（pip install torch torchvision --index-url <官方CUDA源>）")
        return 1

    print(f"{PASS} PyTorch 版本: {torch.__version__}")
    cuda_built = torch.version.cuda
    if not cuda_built:
        print(f"{FAIL} 当前是 CPU 版 torch（torch.version.cuda = None），请卸载后带 --index-url 重装 CUDA 版")
        failed = True
    else:
        print(f"{PASS} 编译时 CUDA : {cuda_built}")
        print(f"{PASS} cuDNN 版本  : {torch.backends.cudnn.version()}")

    # 3. CUDA 可用性
    if not torch.cuda.is_available():
        print(f"{FAIL} torch.cuda.is_available() = False")
        print("       排查顺序: ① nvidia-smi 是否正常 ② torch 是否 CPU 版 ③ 是否在正确的 conda 环境中")
        return 1
    print(f"{PASS} CUDA 可用   : True")
    print(f"{PASS} GPU 数量    : {torch.cuda.device_count()}")
    print(f"{PASS} GPU 名称    : {torch.cuda.get_device_name(0)}")
    props = torch.cuda.get_device_properties(0)
    print(f"{PASS} 计算能力    : sm_{props.major}{props.minor}")
    print(f"{PASS} 显存总量    : {props.total_memory / 1024 ** 3:.1f} GiB")

    # 4. GPU 实际计算测试（整矩阵对比：GPU 结果 vs CPU 全量参考）
    try:
        a = torch.randn(2048, 2048, device="cuda")
        b = torch.randn(2048, 2048, device="cuda")
        c = a @ b
        torch.cuda.synchronize()
        ref = a.cpu() @ b.cpu()   # 必须用完整矩阵做参考；若只取切片相乘，求和范围会被截断导致假报警
        diff = (c.cpu() - ref).abs().max().item()
        rel = diff / (ref.abs().max().item() + 1e-9)
        if rel < 1e-2:
            print(f"{PASS} GPU 矩阵运算: 正常（最大偏差 {diff:.2e}，相对误差 {rel:.1e}）")
        else:
            print(f"{FAIL} GPU 矩阵运算: 结果异常（偏差 {diff}）")
            failed = True
        del a, b, c, ref
        torch.cuda.empty_cache()
    except Exception as e:
        print(f"{FAIL} GPU 矩阵运算: {e}")
        failed = True

    # 5. ultralytics（可选）
    try:
        import ultralytics
        print(f"{PASS} ultralytics : {ultralytics.__version__}")
    except ImportError:
        print("[SKIP] ultralytics 未安装（pip install ultralytics）")

    print("=" * 60)
    if failed:
        print(" 自检未完全通过，请按上方 FAIL 提示排查后再训练")
        return 1
    print(" 自检全部通过，可以开始训练！")
    return 0


if __name__ == "__main__":
    sys.exit(main())
