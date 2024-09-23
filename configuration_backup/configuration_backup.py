#!/usr/bin/env python3

import shutil
import os
import argparse
from datetime import datetime

def search_conf_files(paths, extensions, backup_dir):
    date_format = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    temp_dir = os.path.join('/tmp', 'temp_backup')
    conf_files = []

    # Create the temporary directory
    os.makedirs(temp_dir, exist_ok=True)

    # Create backup directory if not provided
    os.makedirs(backup_dir, exist_ok=True)

    for path in paths:
        for root, _, files in os.walk(path):
            for file in files:
                for extension in extensions:
                    if file.endswith(extension):
                        file_path = os.path.join(root, file)
                        if file_path not in conf_files:  # Avoid duplicates
                            conf_files.append(file_path)
                            shutil.copy(file_path, temp_dir)

    # Creating an archive
    archive_name = f'backup_configurations_{date_format}'
    temp_archive_path = shutil.make_archive(archive_name, 'tar', temp_dir)
    archive_path = os.path.join(backup_dir, f'{archive_name}.tar')
    
    shutil.move(temp_archive_path, backup_dir)  # Move the archive to the target directory
    shutil.rmtree(temp_dir)  # Delete a temporary directory

    print(f"Archieve '{archive_name}' was successfully created to {os.path.relpath(backup_dir)}!\n")

    return conf_files, backup_dir, date_format

def log_file(conf_files, backup_dir, date):
    log_file = os.path.join(backup_dir, f'conf_backup_logs_{date}.log')

    with open(log_file, 'a') as logs:
        logs.write(f"Archive of configurations backup from {date}.\n")
        logs.write("Contains files:\n")
        for conf_file in conf_files:
            logs.write(f"{os.path.realpath(conf_file)}\n")

    return log_file

def main():
    parser = argparse.ArgumentParser(description="Script for copying and archiving backups of configuration files.")
    parser.add_argument('--path', type=str, nargs='+', required=True, help='Specify path(s) to directories with configuration files.')
    parser.add_argument('--extension', type=str, nargs='+', required=True, help='Specify configuration file extension(s).')
    parser.add_argument('--backup_dir', type=str, help='Specify a path to the directory to store configuration backups.', default='/var/backups')
    args = parser.parse_args()

    conf_files, backup_dir, date_format = search_conf_files(args.path, args.extension, args.backup_dir)

    # Check if any files were found before proceeding
    if not conf_files:
        print("No configuration files found. Exiting...")
        return

    log_file_path = log_file(conf_files, backup_dir, date_format)
    
    if os.path.getsize(log_file_path) > 0:
        print(f"Log file '{log_file_path}' was successfully created!")
    else:
        print(f"Log file '{log_file_path}' was not created. Please check file permissions or disk space.")

if __name__ == "__main__":
    main()
