import os
import sys

def count_files_in_directory(directory):
    file_count = 0
    for root, _, files in os.walk(directory):
        file_count += len(files)
    return file_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python filecount.py <directory>")
        sys.exit(1)

    directory_path = sys.argv[1]
    total_files = count_files_in_directory(directory_path)

    print(f"Total files in '{directory_path}': {total_files}")
