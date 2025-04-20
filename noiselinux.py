import os
import sys
import cv2
import numpy as np
from tqdm import tqdm

# Read input/output paths from arguments
input_dir = sys.argv[1]  # e.g., /tmp/data/imagewoof2
output_dir = sys.argv[2]  # e.g., /tmp/data/gauss_imagewoof
os.makedirs(output_dir, exist_ok=True)

def add_gaussian_noise(image, mean=0, std=25):
    gauss = np.random.normal(mean, std, image.shape).astype(np.int16)
    noisy_img = np.clip(image.astype(np.int16) + gauss, 0, 255).astype(np.uint8)
    return noisy_img

for root, dirs, files in os.walk(input_dir):
    rel_path = os.path.relpath(root, input_dir)
    output_subfolder = os.path.join(output_dir, rel_path)
    os.makedirs(output_subfolder, exist_ok=True)

    for filename in tqdm(files, desc=f"Processing {rel_path}", leave=False):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        input_filepath = os.path.join(root, filename)
        image = cv2.imread(input_filepath)

        if image is None:
            continue

        noisy_image = add_gaussian_noise(image)

        output_filename = f"gaussian_{filename}"
        output_filepath = os.path.join(output_subfolder, output_filename)
        cv2.imwrite(output_filepath, noisy_image)
