import os
import shutil
import random

# Define paths
val_dir = r"..\imagewoof2-full\imagewoof2\val"  
test_dir = os.path.join(os.path.dirname(val_dir), "test")  

# Create test directory if it doesn't exist
os.makedirs(test_dir, exist_ok=True)

# Iterate over class subdirectories in val_dir
for class_name in os.listdir(val_dir):
    class_path = os.path.join(val_dir, class_name)
    test_class_path = os.path.join(test_dir, class_name)

    # Skip if not a directory
    if not os.path.isdir(class_path):
        continue

    # Create corresponding class folder in test directory
    os.makedirs(test_class_path, exist_ok=True)

    # Get all image files in the class folder
    images = [img for img in os.listdir(class_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Shuffle and split into two halves
    random.shuffle(images)
    split_index = len(images) // 2  # Split 50/50
    test_images = images[:split_index]  # First half = Test set

    # Move test images to the test directory
    for img in test_images:
        src_path = os.path.join(class_path, img)
        dest_path = os.path.join(test_class_path, img)
        shutil.move(src_path, dest_path)

print("Validation set successfully split into validation & test sets.")
print(f"New test set location: {test_dir}")
