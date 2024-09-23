#!/usr/bin/env python3

import os

# Function to validate if the given path is correct
def validation_path(path):
    return os.path.isdir(path)

def search_files(dir, extension):
    total_files = {}
    
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(extension): # Check file extension
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                total_files[file_path] = file_size

    return total_files.items()

def new_file_record(path, path_to_save, total_files, extension):
    summary_file = os.path.join(path_to_save, "summary.txt")

    with open(summary_file, 'w') as summary:
        summary.write(f"There are {len(total_files)} files with '{extension}' extension in '{os.path.realpath(path)}'.\n\n")
        for file, size in total_files:
            summary.write(f"{file} - {size / 1024:.2f} KB\n")
    return summary_file

def main():
    dir, extension, path_to_save = input("Specify a source path, file extension for search (e.g., .log, .conf), and a path to save the file separated by a space: ").split()

    # Validate the input paths
    if validation_path(dir):
        total_files = search_files(dir, extension)

        if total_files:
            summary = new_file_record(dir, path_to_save, total_files, extension)

            if summary:
                print(f"'{summary}' file successfully created!")
            else:
                print(f"Unable to create '{summary}' file.")
        else:
            print(f"No '{extension}' files found in '{dir}'.")
    else:
            print(f"Directory '{dir}' doesn't exist.")

if __name__ == "__main__":
    main()
