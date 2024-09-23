#!/usr/bin/env python3

import argparse
import os
import re

# Parser object to handle command-line arguments
parser = argparse.ArgumentParser(description="A script that outputs the number of occurrences of a string found in a file.")

# Function to validate if the given path is correct and exists as a file
def validate_path(path):
    # Check if the path matches the regex pattern and if it is a valid file
    return os.path.isfile(path)

# Function to find occurrences of a specified string in a file
def find_string(file_for_search, string):
    pattern = rf'\b{string}\b'  # Regex pattern to match the whole word
    counter = 0

    try:
        with open(file_for_search, 'r') as file:
            for line in file:
                # Find all occurrences of the pattern in each line, case-insensitive
                found_string = re.findall(pattern, line, re.IGNORECASE)
                if found_string:
                    counter += 1  # Increment the counter if the pattern is found
        return counter
    except PermissionError:
        print(f"Access to the '{file_for_search}' file is denied. Please check access to the file.")
        return None

# Main function to parse arguments and call other functions
def main():
    parser = argparse.ArgumentParser(description="A script that outputs the number of occurrences of a string found in a file.")
    parser.add_argument('path', type=str, help='Path to the file to search for.')
    parser.add_argument('string', type=str, help='String or word you need to find in the file.')
    
    args = parser.parse_args()

    # Validate the input file path
    if validate_path(args.path):
        total_entries = find_string(args.path, args.string)
        if total_entries is not None:
            if total_entries > 0:
                print(f"The total amount of '{args.string}' entries in '{args.path}' file is: {total_entries}.")
            else:
                print(f"No '{args.string}' entries in {args.path} file.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
