# service/device.py

import torch

class Device:

    def __init__(self):
        self.value = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
