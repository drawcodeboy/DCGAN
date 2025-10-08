import torch
from torch import nn

class GAN(nn.Module):
    def __init__(self,
                 z_dim=100,
                 img_dim=(1, 28, 28)):
        super().__init__()
        self.generator = Generator()
        self.discriminator = Discriminator()
    
    def forward(self, x):
        pass
    
    @classmethod
    def from_config(cls, cfg):
        return cls(
            z_dim=cfg.get('z_dim', 100),
            img_dim=cfg.get('img_dim', (1, 28, 28))
        )