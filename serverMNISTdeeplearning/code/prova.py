import torch
import os

model_path = os.path.join(os.path.dirname(__file__), "traced_conv.pt")
model = torch.jit.load(model_path)

print(model)