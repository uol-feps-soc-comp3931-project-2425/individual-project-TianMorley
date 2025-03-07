import os
import cv2
from tqdm import tqdm

input_dir = "/kaggle/input/your-dataset"
output_dir = "/kaggle/working/your-dataset-lowres"
os.makedirs(output_dir, exist_ok=True)


def downsample_image(image, scale=4):  # Reduces size by 4x
    h, w = image.shape[:2]
    small = cv2.resize(image, (w // scale, h // scale), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_CUBIC)  # Upscale back

for img_name in tqdm(os.listdir(input_dir), desc="Processing Images"):
    if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue
   
    img_path = os.path.join(input_dir, img_name)
    image = cv2.imread(img_path)

    if image is not None:
        low_res = downsample_image(image)
        cv2.imwrite(os.path.join(output_dir, f"lowres_{img_name}"), low_res)
