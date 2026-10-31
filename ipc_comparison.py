
import psutil
import os

print("IPC MEMORY UTILIZATION ANALYSIS")
print("--------------------------------")

# System memory
memory = psutil.virtual_memory()

print("Total RAM:",
      round(memory.total / (1024**3), 2), "GB")

print("Used RAM:",
      round(memory.used / (1024**3), 2), "GB")

print("Available RAM:",
      round(memory.available / (1024**3), 2), "GB")

print("Memory Utilization:",
      memory.percent, "%")

# Current Python process
process = psutil.Process(os.getpid())

print("\nCURRENT PROCESS INFORMATION")

print("Process ID:", process.pid)

print("Memory Usage:",
      round(process.memory_info().rss / (1024**2), 2), "MB")

print("CPU Usage:",
      process.cpu_percent(interval=1), "%")

print("\nMemory Analysis Completed")
