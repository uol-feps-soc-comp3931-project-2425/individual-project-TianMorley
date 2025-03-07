import cv2
import numpy as np
import os
from tqdm import tqdm

#paths
input_dir = "/kaggle/input/your-dataset"
output_dir = "/kaggle/working/your-dataset-noisy"
os.makedirs(output_dir, exist_ok=True)

def add_gaussian_noise(image, mean=0, std=25):
    gauss = np.random.normal(mean, std, image.shape).astype(np.int16)
    noisy_img = np.clip(image.astype(np.int16) + gauss, 0, 255).astype(np.uint8)
    return noisy_img

# apply noise
for img_name in tqdm(os.listdir(input_dir), desc="Processing Images"):
    if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue  

    img_path = os.path.join(input_dir, img_name)
    image = cv2.imread(img_path)

    if image is not None:
        noisy_gaussian = add_gaussian_noise(image)
        cv2.imwrite(os.path.join(output_dir, f"gaussian_{img_name}"), noisy_gaussian)
