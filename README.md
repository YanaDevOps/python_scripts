# Python Scripts Collection

This repository contains a collection of useful Python scripts for various tasks including system monitoring, backup automation, log analysis, and more. Each script is designed with simplicity and practical utility in mind, making them ideal for automation and general purpose use in system administration.

## Scripts Overview

### 1. **Backup Script**
Automates the process of backing up a specified directory into a compressed archive, with logs for tracking.

- **Location**: `backup/`
- **Usage**: [See detailed README](./backup/README.md)

### 2. **Configuration Backup Script**
Searches for configuration files with specified extensions and archives them for safekeeping.

- **Location**: `configuration_backup/`
- **Usage**: [See detailed README](./configuration_backup/README.md)

### 3. **CPU and Memory Usage Monitor**
Monitors system CPU and memory usage in real-time, providing both a textual report and visual data through charts.

- **Location**: `cpu_memory_usage/`
- **Usage**: [See detailed README](./cpu_memory_usage/README.md)

### 4. **Database Backup Script**
Creates periodic backups of a MySQL database, archiving the backups and recording the process in a log.

- **Location**: `db_backup/`
- **Usage**: [See detailed README](./db_backup/README.md)

### 5. **Directory Size Calculator**
Calculates the total size of all files within a specified directory and provides a summary.

- **Location**: `dir_size/`
- **Usage**: [See detailed README](./dir_size/README.md)

### 6. **Log File Error Extractor**
Scans a specified log file for any errors and outputs the results into a separate log.

- **Location**: `error_logs/`
- **Usage**: [See detailed README](./error_logs/README.md)

### 7. **Errors and Warnings Counter**
Analyzes a system log file, counting the occurrences of errors and warnings and providing the top 5 most frequent messages.

- **Location**: `errors_warnings_counter/`
- **Usage**: [See detailed README](./errors_warnings_counter/README.md)

### 8. **System Monitoring and Logs**
Continuously monitors CPU and memory utilization, generates alerts, and logs the results over time.

- **Location**: `monitoring_logs/`
- **Usage**: [See detailed README](./monitoring_logs/README.md)

### 9. **File Extension Search**
Searches for files with a specified extension within a directory and outputs a summary of the files and their sizes.

- **Location**: `new_file_with_extensions/`
- **Usage**: [See detailed README](./new_file_with_extensions/README.md)

### 10. **Search for Files by Extension**
Searches for all files with a specified extension within a directory and lists their sizes.

- **Location**: `search_for_files_by_extension/`
- **Usage**: [See detailed README](./search_for_files_by_extension/README.md)

### 11. **String Entries in File**
Finds and counts the occurrences of a specific string in a file and lists the matched lines.

- **Location**: `string_entires_in_file/`
- **Usage**: [See detailed README](./string_entires_in_file/README.md)

## Requirements

To run the scripts in this repository, ensure the following:

- **Python**: Version 3.x or later
- **Python Packages**: Some scripts may require additional packages like `psutil`, `argparse`, `logging`, `shutil`, and `matplotlib`. Refer to the individual script READMEs for detailed requirements.
- **MySQL** (for database backup): Ensure that `mysqldump` is installed on the system for the database backup script.

## Installation

1. Clone the repository to your local system:

    ```bash
    git clone git@github.com:YanaDevOps/python_scripts.git
    ```

2. Install required Python packages for the scripts:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the desired script folder and follow the individual README for execution details.

## License

This repository is open-source and free to use under the [MIT License](./LICENSE).

