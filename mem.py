import psutil

# Get RAM usage
ram = psutil.virtual_memory()
# Get Swap usage
swap = psutil.swap_memory()

print(f"RAM Usage: {ram.percent}% : Swap Usage: {swap.percent}%")

partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"Device: {partition.device}, Mountpoint: {partition.mountpoint}, FileSystem: {partition.fstype}")
