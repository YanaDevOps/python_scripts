# Configuration Backup Script

## Description
This script automates the process of backing up configuration files from specified directories and storing them in a tar archive. It allows the user to specify multiple directories and file extensions, then archives the found configuration files and stores them in a specified backup directory. A log file of the operation is created for reference.

## Requirements
- Python 3.x
- `shutil`
- `os`
- `argparse`
- `datetime`

## Usage
```bash
python3 configuration_backup.py --path <path1> <path2> ... --extension <extension1> <extension2> ... [--backup_dir <backup_directory>]
```

## Parameters:
- ```bash --path```: (Required) Specify one or more directories to search for configuration files.
- ```bash --extension```: (Required) Specify one or more file extensions to look for.
- ```bash --backup_dir```: (Optional) Specify a directory where the backup archive will be stored. If not provided, the default is /var/backups.

## Example
```bash
python3 configuration_backup.py --path /etc /usr/local --extension .conf .cfg --backup_dir ./backups
```

## Features
- Supports multiple directories and file extensions.
- Automatically creates a backup directory if it doesn't exist.
- Creates a tar archive of the found configuration files.
- Logs the details of the backup in a log file within the backup directory.
