# CPU and Memory Usage Monitoring Script

## Description
This script retrieves and displays the current CPU utilization and memory usage of the system. It shows CPU usage as a percentage and memory usage details in gigabytes (GB), including total, used, and available memory.

## Requirements
- Python 3.x
- `psutil` module

## Usage
```bash
python3 cpu_mem_usage.py
```

## Example Output
```bash
===== Current CPU utilization =====
CPU utilization percent: 12.0%

===== Current Memory utilization =====
Total memory: 16.00 GB
Used memory: 8.50 GB
Available memory: 7.10 GB
Memory utilization percent: 53.12%
```

## Features
- Displays real-time CPU usage.
- Displays total, used, and available memory in GB.
- Outputs memory usage as a percentage.
