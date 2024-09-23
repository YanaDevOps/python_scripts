#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

# Function to create a backup directory if it doesn't exist
def create_backup_directory(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)

# Function to create a backup of the specified directory
def create_backup(source_dir, backup_dir):
    # Get the current date and time
    date_format = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    # Name of the backup archive
    archive_name = os.path.basename(os.path.normpath(source_dir)) + f"_{date_format}.zip"
    # Create an archive
    backup = shutil.make_archive(archive_name, 'zip', source_dir)
    # Copy the archive to the backup directory
    shutil.move(backup, backup_dir)

    # Write backup details to the log file
    log_file = os.path.join(backup_dir, f"backup_log_{date_format}.txt")
    with open(log_file, 'w') as log:
        log.write(f"Backup created: {archive_name}.zip\n")
        log.write(f"Backuped directory: {os.path.realpath(source_dir)}\n")
        log.write(f"Backup directory: {os.path.realpath(backup_dir)}\n")
        log.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"Your backup '{backup}' was successfully created to '{backup_dir}'!")

# Main script logic
def main():
    main_dir, backup_dir = input("Please, specify by space: \n1) Directory for backup\n2) Backup directory\n").split()
    
    # Validate the input paths
    if os.path.isdir(main_dir):
        # Create backup directory if it does not exist
        create_backup_directory(backup_dir)
        # Perform the backup
        create_backup(main_dir, backup_dir)
    else:
        print("Please, specify correct directory paths (e.g., /your/dir/path).")

if __name__ == "__main__":
    main()
