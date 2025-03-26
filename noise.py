import os
import cv2
import numpy as np
from tqdm import tqdm

# Paths
input_dir = "../imagewoof2-full\imagewoof2"          # e.g., contains subfolders like train/, val/
output_dir = "imagewoofnoisysplit" # Where you'll save the noisy versions
os.makedirs(output_dir, exist_ok=True)

def add_gaussian_noise(image, mean=0, std=25):
    #Gaussian Noise to Image
    # Convert image to int16 to avoid overflow/underflow during addition
    gauss = np.random.normal(mean, std, image.shape).astype(np.int16)
    noisy_img = np.clip(image.astype(np.int16) + gauss, 0, 255).astype(np.uint8)
    return noisy_img

# Walk through all subdirectories and files in the input_dir
for root, dirs, files in os.walk(input_dir):
    # Determine the subdirectory structure relative to `input_dir`
    rel_path = os.path.relpath(root, input_dir)
    # Create an equivalent subdirectory structure in `output_dir`
    output_subfolder = os.path.join(output_dir, rel_path)
    os.makedirs(output_subfolder, exist_ok=True)
    
    # Process all files in the current folder
    for filename in tqdm(files, desc=f"Processing {rel_path}", leave=False):
        # Check if it's an image file (by extension)
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
        
        # Read the image
        input_filepath = os.path.join(root, filename)
        image = cv2.imread(input_filepath)
        
        if image is None:
            continue
        
        # Add Gaussian noise
        noisy_image = add_gaussian_noise(image)
        
        # Build the output file path and save
        output_filename = f"gaussian_{filename}"
        output_filepath = os.path.join(output_subfolder, output_filename)
        cv2.imwrite(output_filepath, noisy_image)
