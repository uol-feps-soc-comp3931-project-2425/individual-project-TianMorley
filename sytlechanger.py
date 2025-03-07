import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.models import vgg19
from PIL import Image
import numpy as np
import os

# Adaptive Instance Normalization function
def adain(content_features, style_features, alpha=1.0):
    """Performs Adaptive Instance Normalization (AdaIN)"""
    content_mean, content_std = content_features.mean([2, 3], keepdim=True), content_features.std([2, 3], keepdim=True)
    style_mean, style_std = style_features.mean([2, 3], keepdim=True), style_features.std([2, 3], keepdim=True)
    
    normalized_content = (content_features - content_mean) / content_std
    stylized_content = normalized_content * style_std + style_mean
    return alpha * stylized_content + (1 - alpha) * content_features

# Load Pretrained VGG19 Model
class VGGEncoder(nn.Module):
    def __init__(self):
        super(VGGEncoder, self).__init__()
        vgg = vgg19(pretrained=True).features
        self.enc_layers = nn.Sequential(*list(vgg.children())[:21])  # Extract up to relu4_1
        for param in self.enc_layers.parameters():
            param.requires_grad = False  # Freeze weights

    def forward(self, x):
        return self.enc_layers(x)

# Load Image Function
def load_image(image_path, size=256):
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # Add batch dimension

# Apply Style Transfer
def style_transfer(content_path, style_path, output_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    vgg_encoder = VGGEncoder().to(device).eval()

    content_img = load_image(content_path).to(device)
    style_img = load_image(style_path).to(device)

    content_features = vgg_encoder(content_img)
    style_features = vgg_encoder(style_img)

    stylized_img = adain(content_features, style_features)
    
    # Convert tensor back to image
    stylized_img = stylized_img.squeeze(0).detach().cpu().numpy()
    stylized_img = np.transpose(stylized_img, (1, 2, 0))
    stylized_img = np.clip(stylized_img, 0, 1)

    Image.fromarray((stylized_img * 255).astype(np.uint8)).save(output_path)

# Example Usage
content_img_path = "/kaggle/input/tsinghua-dogs/sample.jpg"
style_img_path = "/kaggle/input/styles/night_style.jpg"  # Nighttime filter
output_img_path = "/kaggle/working/stylized_dog.jpg"

style_transfer(content_img_path, style_img_path, output_img_path)

