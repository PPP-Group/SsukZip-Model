import torch

DEVICE = torch.cuda.is_available()
print(f'{DEVICE}, {torch.__version__}')