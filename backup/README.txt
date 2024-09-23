# README for Backup Script

## Overview:
This script automates creating a backup by compressing a specified directory into a `.zip` archive and storing it in a designated backup directory. It also generates a log file detailing the backup.

## Requirements:
- Python 3.x (no external modules required)

## Usage:
1. Run the script.
2. Input two paths when prompted:
   - Source directory (the folder to back up)
   - Backup directory (where the backup archive will be stored)

Example:
```bash
python3 backup.py
Please, specify by space: 
1) Directory for backup
2) Backup directory
./source_directory /backup_directory
```

## Features:
- create_backup_directory(path): Creates the backup directory if it doesn't exist.
- create_backup(source_dir, backup_dir): Compresses the source directory into a .zip archive and moves it to the backup directory. A log file is generated detailing the operation.

## Output:
- Archive file: ```bash source_directory_YYYY-MM-DD_HH-MM-SS.zip```
- Log file: ```bash backup_log_YYYY-MM-DD_HH-MM-SS.txt```
