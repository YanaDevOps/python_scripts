# File Search by Extension Script

## Description
This script searches for all files with a specified extension in a given directory and displays their paths and sizes. It is useful for quickly finding files of a particular type, such as configuration files, logs, or text files, within a directory and its subdirectories.

## Requirements
- Python 3.x

## Usage
```bash
python3 search_for_files_by_extension.py
```

You will be prompted to enter the directory path and file extension for the search.

## Example
```bash
Specify a path and file extension (e.g., .txt) separated by a space: /etc/ .conf
===== All '.conf' files in the '/etc/' =====
/etc/apache2/apache2.conf - 14.80 KB
/etc/sysctl.conf - 2.52 KB
```

## Features
- Recursively searches through the specified directory and subdirectories.
- Displays the file path and size for each file with the specified extension.

## Limitations
- The script only searches for files that match the given extension.
