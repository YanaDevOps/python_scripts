#!/usr/bin/env python3

import argparse
import os
import re

# Function to validate if the given path is correct and exists as a file
def validate_path(path):
    return os.path.isfile(path)

# Function to find occurrences of a specified string in a file
def find_string(file_for_search, string):
    pattern = rf'\b{string}\b'  # Regex pattern to match the whole word
    counter = 0
    matching_lines = []  # List to store lines with matches

    try:
        with open(file_for_search, 'r') as file:
            for line in file:
                # Find all occurrences of the pattern in each line, case-insensitive
                if re.search(pattern, line, re.IGNORECASE):
                    counter += 1  # Increment the counter if the pattern is found
                    matching_lines.append(line.strip())  # Store the matched line

        return counter, matching_lines
    except PermissionError:
        print(f"Access to the '{file_for_search}' file is denied. Please check access to the file.")
        return None, None

# Main function to parse arguments and call other functions
def main():
    parser = argparse.ArgumentParser(description="A script that outputs the number of occurrences of a string found in a file.")
    parser.add_argument('path', type=str, help='Path to the file to search for.')
    parser.add_argument('string', type=str, help='String or word you need to find in the file.')
    
    args = parser.parse_args()

    # Validate the input file path
    if validate_path(args.path):
        total_entries, matching_lines = find_string(args.path, args.string)
        if total_entries is not None:
            if total_entries > 0:
                print(f"The total amount of '{args.string}' entries in '{args.path}' file is: {total_entries}:\n")
                print("Matching lines:")
                for line in matching_lines:
                    print(line)
            else:
                print(f"No '{args.string}' entries in '{args.path}' file.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
