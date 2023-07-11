import torch

def get_torch_version():
    return f"Pytorch version: {torch.__version__}. Cuda: {torch.cuda.is_available()}. GPU device: {torch.cuda.current_device()}. GPU name: {torch.cuda.get_device_name(0)}"