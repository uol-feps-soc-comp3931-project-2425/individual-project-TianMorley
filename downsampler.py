import os
import cv2
from tqdm import tqdm

input_root = r"../imagewoof2-full/imagewoof2"
output_root = r"../imagewoof2-lowres"
os.makedirs(output_root, exist_ok=True)

def downsample_image(image, scale=10):
    h, w = image.shape[:2]
    small = cv2.resize(image, (w // scale, h // scale), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_CUBIC)

print(" Starting recursive downsampling...")

for root, _, files in os.walk(input_root):
    rel_path = os.path.relpath(root, input_root)
    output_dir = os.path.join(output_root, rel_path)
    os.makedirs(output_dir, exist_ok=True)

    for img_name in tqdm(files, desc=f" Processing {rel_path}", leave=False):
        if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
            print(f" Skipping unsupported file: {img_name}")
            continue

        img_path = os.path.join(root, img_name)
        out_path = os.path.join(output_dir, img_name)

        image = cv2.imread(img_path)
        if image is None:
            print(f"Failed to read: {img_path}")
            continue

        low_res = downsample_image(image, scale=10)  
        success = cv2.imwrite(out_path, low_res)

        if success:
            print(f" Saved: {out_path}")
        else:
            print(f"Failed to save: {out_path}")
