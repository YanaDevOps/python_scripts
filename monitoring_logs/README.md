# CPU and Memory Usage Monitoring Script

## Description
This Python script monitors system CPU and memory usage, logs the data at regular intervals, and generates a visual plot at the end of each day or when manually stopped. It can trigger alerts if CPU or memory usage exceeds specified thresholds.

## Requirements
- Python 3.x
- `psutil` module
- `matplotlib` module

## Usage
```bash
python3 monitoring_logs.py <log_directory_path> <time_interval_in_minutes>
```

## Example
```bash
python3 monitoring_logs.py /home/user/logs 5
```

## Features
- Monitors CPU and memory usage.
- Logs data to a file.
- Creates daily usage graphs.
