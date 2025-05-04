import os

# Path to the root of dataset
dataset_root = r"..\imagewoof2-full\imagewoof2"  

#rename breeds
synset_to_breed = {
    'n02086240': 'Shih-Tzu',
    'n02087394': 'Rhodesian Ridgeback',
    'n02088364': 'Beagle',
    'n02089973': 'English Foxhound',
    'n02093754': 'Australian Terrier',
    'n02096294': 'Border Terrier',
    'n02099601': 'Golden Retriever',
    'n02105641': 'Old English Sheepdog',
    'n02111889': 'Samoyed',
    'n02115641': 'Dingo'
}

# Dataset splits
splits = ['train', 'val', 'test']

for split in splits:
    split_path = os.path.join(dataset_root, split)
    print(f"\nChecking split: {split_path}")

    if not os.path.isdir(split_path):
        print(f"Directory not found: {split_path} — skipping.")
        continue

    for folder in os.listdir(split_path):
        folder_path = os.path.join(split_path, folder)
        print(f"Inspecting: {folder_path}")

        if not os.path.isdir(folder_path):
            print(f"Not a directory — skipping.")
            continue

        if '-' in folder:
            print(f"Already renamed — skipping.")
            continue

        if folder in synset_to_breed:
            breed_name = synset_to_breed[folder]
            new_folder_name = f"{folder}-{breed_name}"
            new_folder_path = os.path.join(split_path, new_folder_name)

            print(f"Renaming to: {new_folder_name}")
            try:
                os.rename(folder_path, new_folder_path)
                print(f"Renamed successfully.")
            except Exception as e:
                print(f"Rename failed: {e}")
        else:
            print(f"No mapping found for: {folder} — skipping.")
