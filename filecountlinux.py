import os
import sys

def count_files_in_directory(directory):
    file_count = 0
    for root, _, files in os.walk(directory):
        file_count += len(files)
    return file_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python filecount.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]

    total = 0
    for subfolder in os.listdir(root_dir):
        sub_path = os.path.join(root_dir, subfolder)
        if os.path.isdir(sub_path):
            count = count_files_in_directory(sub_path)
            print(f"{subfolder}: {count} files")
            total += count

    print(f"Total files in '{root_dir}': {total}")
