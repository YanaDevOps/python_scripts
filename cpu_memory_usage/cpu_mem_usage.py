#!/usr/bin/env python3

import psutil

print("===== Current CPU utilization =====")
print(f"CPU utilization percent: {psutil.cpu_percent(interval=1, percpu=False)}%\n")

print("===== Current Memory utilization =====")
memory = psutil.virtual_memory()
print(f"Total memory: {memory.total / (1024 ** 3):.2f} GB")
print(f"Used memory: {memory.used / (1024 ** 3):.2f} GB")
print(f"Available memory: {memory.available / (1024 ** 3):.2f} GB")
print(f"Memory utilization percent: {memory.percent}%")
