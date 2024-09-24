#!/usr/bin/env python3

import os

def search_files(dir, extension):
    total_files = {} # Dictionary of files' extensions

    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(extension): # Check file extension
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    total_files[file_path] = file_size

    return total_files.items()

# Main script logic
def main():
    dir, extension = input("Specify a path and file extension (e.g., .txt) separated by a space: ").split()

    # Check if this dir exists
    if os.path.isdir(dir):
        total_files = search_files(dir, extension)
        # Output all files with the specified extension
        if total_files:
            print(f"===== All '{extension}' files in the '{dir}' =====")
            for path, size in total_files:
                print(f"{path} - {size / 1024:.2f} KB")
        else:
            print(f"No '{extension}' files found in '{dir}'.")
    else:
        print(f"Directory '{dir}' doesn't exist.")

# Entry point of the script
if __name__ == "__main__":
    main()
