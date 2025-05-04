import os

def count_files_in_directory(directory):
    file_count = 0
    for root, _, files in os.walk(directory):
        file_count += len(files)
    return file_count

# Example usage
directory_path = r"..\imagewoof2-full\imagewoof2\test"
total_files = count_files_in_directory(directory_path)

print(f"Total files in '{directory_path}': {total_files}")
