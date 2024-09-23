#!/usr/bin/env python3

import re
import os
from collections import Counter

error_pattern = r'\berror\b'
errors = []

log_file = input("Specify the path to your log file to analyze: ")
logs_dir = os.path.normpath(input("Specify the path to store your errors log file: "))
errors_file = f'{os.path.realpath(logs_dir)}/{os.path.basename(log_file)}_error_logs.txt'

# Create logs_dir if it doesn't excist
if not os.path.isdir(logs_dir):
    os.makedirs(logs_dir, exist_ok=True)

# Check if this file excists
if os.path.exists(log_file):
    try:
        with open(log_file, 'r') as logs:
            for line in logs:
                if re.search(error_pattern, line, re.IGNORECASE):  # Look for the word “error” in the line
                    errors.append(line.strip()) # Save the full string

            if errors:
                with open(errors_file, 'w') as error_logs:
                    for error in errors:
                        error_logs.write(error + "\n")
                print(f"Total amount of errors: {len(errors)}.\n")
                print(f"Errors written to '{errors_file}'.")
            else:
                print("No errors found in the log file.")
    except IsADirectoryError:
        print(f"Is a directory: {log_file}. Specify the correct path to your log file.")
else :
    print(f"{os.path.basename(log_file)} doesn't excists. Please specify the correct path.")
