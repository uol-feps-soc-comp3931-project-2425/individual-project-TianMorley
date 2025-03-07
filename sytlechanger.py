import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.models import vgg19
from PIL import Image
import numpy as np
import os

# adaptive instance normalisation function
def adain(content_features, style_features, alpha=1.0):
    content_mean, content_std = content_features.mean([2, 3], keepdim=True), content_features.std([2, 3], keepdim=True)
    style_mean, style_std = style_features.mean([2, 3], keepdim=True), style_features.std([2, 3], keepdim=True)

    normalized_content = (content_features - content_mean) / (content_std + 1e-7)
    stylized_content = normalized_content * style_std + style_mean
    return alpha * stylized_content + (1 - alpha) * content_features

# load VGG model (pretrained)
class VGGEncoder(nn.Module):
    def __init__(self):
        super(VGGEncoder, self).__init__()
        vgg = vgg19(pretrained=True).features
        self.enc_layers = nn.Sequential(*list(vgg.children())[:21])  # Extract up to relu4_1
        for param in self.enc_layers.parameters():
            param.requires_grad = False  # freeze weighting
            
    def forward(self, x):
        return self.enc_layers(x)

def load_image(image_path, size=256):
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # add batch dimension

def tensor_to_image(tensor):
    tensor = tensor.squeeze(0).detach().cpu().numpy()
    tensor = np.transpose(tensor, (1, 2, 0))

    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    
    tensor = (tensor * std) + mean  # unnormalise
    tensor = np.clip(tensor, 0, 1)
    
    return Image.fromarray((tensor * 255).astype(np.uint8))

# apply style
def style_transfer(content_path, style_path, output_path, alpha=1.0):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    vgg_encoder = VGGEncoder().to(device).eval()

    content_img = load_image(content_path).to(device)
    style_img = load_image(style_path).to(device)

    content_features = vgg_encoder(content_img)
    style_features = vgg_encoder(style_img)

    stylized_img = adain(content_features, style_features, alpha)
    
    # convert tensor back
    stylized_image = tensor_to_image(stylized_img)
    stylized_image.save(output_path)

content_img_path = "/kaggle/input/tsinghua-dogs/sample.jpg"
style_img_path = "/kaggle/input/styles/night_style.jpg"  # Nighttime filter
output_img_path = "/kaggle/working/stylised_dog.jpg"

style_transfer(content_img_path, style_img_path, output_img_path, alpha=0.8)


