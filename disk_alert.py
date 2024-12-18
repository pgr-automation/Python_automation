import shutil

# Check disk usage
total, used, free = shutil.disk_usage("/")
threshold = 350 * 1024 * 1024 * 1024  # 10 GB

# Convert bytes to GB
free_gb = free / (1024 ** 3)  # 1 GB = 1024^3 bytes
threshold_gb = threshold / (1024 ** 3)

if free < threshold:
    print(f"Free space: {free_gb:.2f} GB")
