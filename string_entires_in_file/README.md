# String Occurrence Finder

## Description
This Python script searches for a specific string or word in a specified file, counts how many times the string occurs, and outputs the matching lines where the string was found. It's useful for quickly finding and analyzing specific content in large text files or logs.

## Requirements
- Python 3.x
- No additional modules are required.

## Usage
```bash
python3 string_occurrences.py <file_path> <string>
```

## Parameters
```bash 
file_path
```
The path to the file you want to search in.
```bash
string
```
The string or word you want to search for.

## Example
```bash
python3 string_occurrences.py /var/log/syslog error
```

## Output
- The script prints the total number of occurrences of the string in the file.
- It also prints each line where the string was found.
