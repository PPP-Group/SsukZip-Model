import torch

DEVICE = torch.cuda.is_available()
print(f'{DEVICE}, {torch.__version__}')
print(f'{torch.cuda.current_device()}')
print(f'{torch.cuda.device_count()}')
print(f'{torch.cuda.get_device_name(0)}')