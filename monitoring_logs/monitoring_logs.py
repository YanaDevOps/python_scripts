#!/usr/bin/env python3

import os
import time
import psutil
import matplotlib.pyplot as plt
import argparse
from datetime import datetime

CPU_THRESHOLD = 80  # Percentage threshold value
MEMORY_THRESHOLD = 80

# Placeholder lists for data collection
cpu_data = []
memory_data = []

# Function to create a directory if it doesn't exist
def validate_path(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    return True

# Function to check CPU and memory usage against thresholds
def cpu_mem_threshold():
    alerts = []
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"ALERT! CPU utilization exceeds {CPU_THRESHOLD}% (current value: {cpu_usage}%)")

    if memory_usage > MEMORY_THRESHOLD:
        alerts.append(f"ALERT! Memory utilization exceeds {MEMORY_THRESHOLD}% (current value: {memory_usage}%)")

    return "\n".join(alerts) if alerts else "No alerts."

# Function for data visualization
def data_visualization(path):
    times = [i for i in range(len(cpu_data))]

    plt.figure(figsize=(10, 6))
    plt.plot(times, cpu_data, label='CPU Usage (%)', color='blue')
    plt.plot(times, memory_data, label='Memory Usage (%)', color='green')

    plt.xlabel('Time Intervals')
    plt.ylabel('Usage (%)')
    plt.title(f'System Usage for {datetime.now().strftime("%Y-%m-%d")}')
    plt.legend()
    plt.grid(True)

    plt.savefig(os.path.join(path, f'usage_plot_{datetime.now().strftime("%Y-%m-%d")}.png'))
    plt.close()

# Function for writing system data (CPU and memory usage) to a log file
def monitoring(path, time_interval):
    log_file = os.path.join(path, 'system_monitor.log')  # Define the log file path

    try:
        with open(log_file, 'a') as logs:  # Open the log file in append mode
            try:
                while True:  # Start an infinite loop for continuous monitoring
                    cpu_usage = psutil.cpu_percent()
                    memory_usage = psutil.virtual_memory().percent

                    logs.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    logs.write(f"CPU Usage: {cpu_usage}%\n")
                    logs.write(f"Memory Usage: {memory_usage}%\n")
                    logs.write(f"Alerts: {cpu_mem_threshold()}\n\n")

                    cpu_data.append(cpu_usage)
                    memory_data.append(memory_usage)

                    current_time = datetime.now().strftime('%H:%M')
                    
                    # Check if it's the end of the day
                    if current_time == "23:59":
                        data_visualization(path)
                        cpu_data.clear()
                        memory_data.clear()

                    # Converting minutes into seconds
                    time.sleep(time_interval * 60)
            except KeyboardInterrupt:  # Handle script interruption (e.g., Ctrl+C)
                data_visualization(path)  # Visualize collected data before exit
                logs.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -- Monitoring script closed by user.\n")
                print(f"The monitoring script has been interrupted. Check the '{log_file}' file.")
    except (OSError, IOError) as e:  # Handle errors related to file operations
        print(f"Error while opening file: {e}")

# Main function to handle user input and start monitoring
def main():
    parser = argparse.ArgumentParser(description="The script accepts a directory path to save the system monitoring logs.")
    parser.add_argument('path', type=str, help='Path to the directory to save the system monitoring logs.')
    parser.add_argument('time', type=int, help='Frequency of system utilization check and logging. In minutes.')

    args = parser.parse_args()

    if validate_path(args.path):
        try:
            monitoring(args.path, args.time)
        except KeyboardInterrupt:
            print("Monitoring stopped.")
    else:
        print("Please, specify the correct directory path (e.g., /your/dir/path).")

# Entry point of the script
if __name__ == "__main__":
    main()
