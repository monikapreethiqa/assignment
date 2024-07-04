import psutil
import datetime
# usage definition
cpu_space = 80
memory_space = 80
disk_space = 90

def get_cpu_usage():
    return psutil.cpu_percent()
def get_memory_usage():
    return psutil.virtual_memory().percent
def get_disk_usage(mountpoint ="/"):
    disk_usage = psutil.disk_usage(mountpoint)
    return disk_usage.percent
def write_alert(message):
    timestamp = datetime.datetime.now().strftime("%y-%m-%d %HH:%MM:%SS")
    with open("console_file.log", "a") as f:
        f.write(f"{timestamp} -- {message} \n")
#server information
cpu_threshold = get_cpu_usage()
memory_threshold = get_memory_usage()
disk_threshold = get_disk_usage()
#write alert to log file
if cpu_threshold > cpu_space:
    write_alert(f"CPU usage Exceeded: {cpu_threshold}%")
if disk_threshold > disk_space:
    write_alert(f"DISK SPACE Exceeded: {disk_threshold}% on {mountpoint}")
if memory_threshold > memory_space:
    write_alert(f"Memory usage Exceeded: {memory_threshold}%")