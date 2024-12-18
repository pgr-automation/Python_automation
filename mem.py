import psutil

# Get RAM usage
ram = psutil.virtual_memory()
# Get Swap usage
swap = psutil.swap_memory()

print(f"RAM Usage: {ram.percent}% : Swap Usage: {swap.percent}%")
