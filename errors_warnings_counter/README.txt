# Syslog Error and Warning Analysis Script

## Description
This script analyzes the system log file (`/var/log/syslog`) to find and count all occurrences of errors and warnings. It also identifies the top 5 most common errors and warnings.

## Requirements
- Python 3.x

## Usage
```bash
python3 syslog_analysis.py
```

## Features
- Scans for "error" and "warning" keywords in the syslog.
- Counts the total number of errors and warnings.
- Outputs the top 5 most frequent errors and warnings.
