# Log File Error Analysis Script

## Description
This script scans a specified log file for occurrences of the word "error" and saves the lines containing these errors into a separate log file. It helps in identifying errors from large system or application logs.

## Requirements
- Python 3.x

## Usage
```bash
python3 error_logs.py
```

## Parameters
- The script will prompt for:
   * The path to the log file to analyze.
   * The path where the errors log file will be stored.

## Features
- Searches for the keyword "error" in the log file.
- Saves lines with errors to a new log file.
- Reports the total number of errors found.
