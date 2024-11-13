import csv
import subprocess
import platform

# Function to get the server IP address using 'hostname -I | awk'
def get_server_ip():
    try:
        # Run the shell command to get the server's IP address
        server_ip = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True).decode('utf-8').strip()
        return server_ip
    except subprocess.CalledProcessError as e:
        print(f"Error getting server IP: {e}")
        return "Unknown"

# Function to check if the OS is Red Hat family
def is_redhat_family():
    try:
        # Get the OS distribution family from /etc/os-release or 'platform' library
        distro = platform.linux_distribution()[0].lower()
        if 'redhat' in distro or 'centos' in distro or 'fedora' in distro:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking OS family: {e}")
        return False

# Function to check disk usage for all mounted filesystems and save in CSV format if usage > 85%
def check_disk_usage_csv(output_file='disk_usage.csv', threshold=85):
    print("Checking disk usage for all mounted filesystems...")
    
    # Run the 'df' command to get disk usage for all mounted filesystems
    disk_usage = subprocess.check_output(['df', '-h']).decode('utf-8').splitlines()
    
    # Get the server's IP address using the shell command
    server_ip = get_server_ip()
    
    # Open the CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header with an additional "Server IP" column
        writer.writerow(['Server IP', 'Filesystem', 'Size', 'Used', 'Available', 'Use%', 'Mounted on'])
        
        # Loop through the lines of df output (skipping the header)
        for line in disk_usage[1:]:
            fields = line.split()
            
            # Extract the 'Use%' value and remove the '%' sign to convert to an integer
            usage_percentage = int(fields[4].replace('%', ''))
            
            # If the usage is greater than the threshold, write to CSV
            if usage_percentage > threshold:
                # Add server IP as the first column
                writer.writerow([server_ip] + fields)

    print(f"Disk usage information (above {threshold}%) has been saved to '{output_file}'.")

# Main function to run the disk usage check only if the OS is Red Hat family
def main():
    if is_redhat_family():
        check_disk_usage_csv('disk_usage.csv', threshold=85)
    else:
        print("This script is intended to run only on Red Hat family systems (RHEL, CentOS, Fedora).")

if __name__ == "__main__":
    main()

