#!/usr/bin/env python3

import os

dir_path = input("Specify the directory path: ")
total_size = 0

# Check if this dir exists
if os.path.isdir(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
        
    print(f"The total size of all files in '{dir_path}' is: {total_size / (1024 * 1024):.2f} MB")
else:
    print(f"Directory '{dir_path}' doesn't excist.")
