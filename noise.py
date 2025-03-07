import cv2
import numpy as np
import os
from tqdm import tqdm


# paths
input_dir = "/kaggle/input/your-dataset" 
output_dir = "/kaggle/working/your-dataset-noisy"
os.makedirs(output_dir, exist_ok=True)

# add Gaussian noise
def add_gaussian_noise(image, mean=0, std=25):
    gauss = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_img = cv2.add(image, gauss)
    return noisy_img

# Function to add salt-and-pepper noise
def add_salt_pepper_noise(image, prob=0.02):
    noisy_img = np.copy(image)
    total_pixels = image.size
    num_salt = int(total_pixels * prob / 2)
    num_pepper = int(total_pixels * prob / 2)

    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy_img[coords[0], coords[1]] = 255

    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy_img[coords[0], coords[1]] = 0
    return noisy_img

# add noise
for img_name in tqdm(os.listdir(input_dir)):
    img_path = os.path.join(input_dir, img_name)
    image = cv2.imread(img_path)

    if image is not None:
        noisy_gaussian = add_gaussian_noise(image)
        noisy_sp = add_salt_pepper_noise(image)

        cv2.imwrite(os.path.join(output_dir, f"gaussian_{img_name}"), noisy_gaussian)
        cv2.imwrite(os.path.join(output_dir, f"sp_{img_name}"), noisy_sp)
