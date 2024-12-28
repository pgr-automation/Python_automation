import json

def gather_details():
    filename = 'describe-instances.json'
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            # Parse the JSON content
            details = json.load(file)
            
            # Print the entire JSON structure
            #print(json.dumps(details, indent=2))
            
            # Iterate over reservations and instances
            for reservation in details.get('Reservations', []):
                for instance in reservation.get('Instances', []):
                    #print(instance)  # Print each instance's details
                    if ImageId := instance.get('ImageId'):
                        print(f"Image ID: {ImageId}")
                    if InstanceType := instance.get('InstanceType'):
                        print(f"Instance Type: {InstanceType}")
                    if State := instance.get('State', {}).get('Name'):
                        print(f"State: {State}")
                    if PublicIpAddress := instance.get('PublicIpAddress'):
                        print(f"Public IP Address: {PublicIpAddress}")

                        print(f"Private IP Address: {instance.get('PrivateIpAddress')}, "
                              f"Launch Time: {instance.get('LaunchTime')}, SSH_Key_Name: {instance.get('KeyName')}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")

gather_details()
