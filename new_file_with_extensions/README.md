# File Search and Summary Script

## Description
This Python script searches for files with a specified extension in a given directory, calculates their size, and creates a summary file with details about the found files. The summary includes the file paths and sizes, and it is saved to a specified directory.

## Requirements
- Python 3.x

## Usage
```bash
python3 file_search.py
```

You will be prompted to provide:
1. Source directory path
3. File extension to search for (e.g., .log, .conf)
4. Directory to save the summary file

## Example
```bash
Specify a source path, file extension for search (e.g., .log, .conf), and a path to save the file separated by a space:
./logs .log ./summary
```

## Features
- Recursively searches through directories for files with a specified extension.
- Creates a summary of the found files, including file size.
