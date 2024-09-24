# MySQL Database Backup Script

## Description
This script automates the process of backing up a MySQL database at regular intervals. It supports customization of the backup frequency, connection details, and storage location for the backups. The script creates a SQL dump of the specified database, logs the backup process, and can handle interruptions.

## Requirements
- Python 3
- MySQL installed and running
- The `mysqldump` utility available in your system
- Required Python modules:
    - argparse
    - logging
    - shutil
    - os
    - datetime

## Usage
```bash
python3 db_backup.py --db_name <db_name> --user_name <user_name> --host <host> --backup_path <backup_path> --copy_frequency <frequency_in_minutes>
```

## Parameters:
* --db_name: (Required) The name of the MySQL database to back up.
* --user_name: (Required) The MySQL username with sufficient permissions.
* --host: (Required) The MySQL host (e.g., localhost).
* --port: (Optional) The MySQL port. Defaults to 3306.
* --backup_path: (Required) The directory where backups and logs will be stored.
* --copy_frequency: (Required) The interval between backups, in minutes.

## Example
```bash
python3 db_backup.py --db_name test_db --user_name root --host localhost --backup_path /var/backups --copy_frequency 60
```

## Features
* Backs up a MySQL database to the specified directory at regular intervals.
* Logs all backup operations in a rotating log file (mysql_backup.log).
* Generates SQL dump files with timestamped filenames.
* Handles script interruptions and logs critical errors.

## Setup
Ensure you have the required Python modules installed:
```bash
pip install argparse logging psutil
```
