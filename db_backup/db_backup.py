#!/usr/bin/env python3

import argparse
import subprocess
import os
import time
import logging
import logging.handlers as handlers
from datetime import datetime
from getpass import getpass

# Define the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Function to set up logging
def setup_logger(log_path):
    # Create log file path
    log_file = os.path.join(log_path, 'mysql_backup.log')

    # Create a handler to write to the file with rotation
    file_handler = handlers.RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

def mysql_backup(db_name, user_name, host, port, password, backup_path, copy_frequency):     
    command = [
        'mysqldump',
        '-h', host,
        '-P', str(port),
        '-u', user_name,
        db_name
    ]

    # Create a backup directory if it does not exist
    os.makedirs(backup_path, exist_ok=True)

    # Set the environment variable for the password
    env = os.environ.copy()
    env['MYSQL_PWD'] = password

    copy_frequency *= 60  # Converting minutes to seconds

    logger.info("Starting database backup process.")

    try:
        while True:
            try:
                # Form the name of the backup file inside the loop
                date_format = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                backup_file = os.path.join(backup_path, f'mysql_backup_{date_format}.sql')
                try:
                    with open(backup_file, 'w') as file:
                        result = subprocess.run(command, stdout=file, check=True, env=env)
                        if result.returncode == 0:
                            logger.info("Connected to the database successfully.")
                        else:
                            logger.error("Unable to connect to the database.")
                except (IOError, OSError) as file_error:
                    logger.exception(f"Failed to open/create '{backup_file}' file: {file_error}")

                print(f"Backup of database '{db_name}' has been successfully created. Check the file '{backup_file}'.")
            except subprocess.CalledProcessError as error:
                print(f"Backup process failed due to a critical error. Check the log file '{os.path.join(backup_path, 'mysql_backup.log')}'.")
                logger.critical(f"Backup process failed due to a critical error: {error}")

            logger.info("Backup process completed.")
            time.sleep(copy_frequency)
            logger.info(f"The next backup process starts in {copy_frequency} seconds.")

    except KeyboardInterrupt:  # Handle script interruption (e.g., Ctrl+C)
        logger.warning(f"Database backup script has been interrupted. Check the '{backup_file}' file.")

def main():
    parser = argparse.ArgumentParser(description="Script for database backup.")
    parser.add_argument('--db_name', type=str, required=True, help='Specify the database name.')
    parser.add_argument('--user_name', type=str, required=True, help='Specify the username.')
    parser.add_argument('--host', type=str, required=True, help='Specify the host for database connection.')
    parser.add_argument('--port', type=int, default=3306, help='Specify the port for database connection.')
    parser.add_argument('--backup_path', type=str, default='/var/backups', help='Specify a path to the directory to store database backups.')
    parser.add_argument('--copy_frequency', type=int, default=120, help='Specify the backup frequency in minutes.')

    args = parser.parse_args()

    setup_logger(args.backup_path)

    password = getpass("Enter your password: ")  # Get the user password without displaying it on the command line
    logger.info("Password entered. It is hidden in the output of this script.")

    mysql_backup(args.db_name, args.user_name, args.host, args.port, password, args.backup_path, args.copy_frequency)

if __name__ == "__main__":
    main()
