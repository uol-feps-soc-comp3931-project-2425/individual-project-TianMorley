# Project Notebooks

This directory contains all the Jupyter notebooks used during the project. Each notebook serves a specific purpose, either for model training, experimentation, or for documenting an approach included in the report. 

All the cells are required to run in order or the code will fail. The paths for datasets also must be changed for whichever dataset you are using. 

```python
## Deit-Small

Denotes the standardised training pipeline. To use it with a different model, replace the `load_model` section with your relevant model:

# ConvNeXt-Tiny
from torchvision.models import convnext_tiny
model = convnext_tiny()

# DeiT III Small
from timm import create_model
model = create_model('deit3_small_patch16_224', pretrained=True)

# Swin-Tiny
from timm import create_model
model = create_model('swin_tiny_patch4_window7_224', pretrained=True)

# EfficientNetV2-Small
from timm import create_model
model = create_model('efficientnetv2_s', pretrained=True)

# Project Notebooks

## convnext-kfold

Denotes the k-fold pipeline implementation, which was scrapped from the final pipeline. Its inclusion here is for reproducibility of explanations in the report.

## VMambaTM

The VMambaTM notebook is separate due to having different requirements for running. The notebook trains as implemented, but if you want to load a checkpoint, you must add the `--resume` command-line argument with the path to your checkpoint.

To test a checkpoint, you must use both `--eval` and `--resume`, specifying the checkpoint path you want to evaluate.



