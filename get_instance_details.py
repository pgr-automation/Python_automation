import boto3

def list_ec2_instances(region):
    # Create an EC2 resource with the specified region
    ec2 = boto3.resource('ec2', region_name=region)

    # Retrieve all EC2 instances
    instances = ec2.instances.all()
    # Print instance details
    for instance in instances:
        print(f"Instance ID: {instance.id}")
        print(f"Instance Type: {instance.instance_type}")
        print(f"State: {instance.state['Name']}")
        print(f"Public IP: {instance.public_ip_address}")
        print(f"Private IP: {instance.private_ip_address}")
        print(f"Launch Time: {instance.launch_time}")
        name_tag = None
        if instance.tags:
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    name_tag = tag['Value']
                    break  # Stop searching once we find the Name tag
        print(f"Name: {name_tag if name_tag else 'No Name tag found'}")

        project_tag = None
        if instance.tags:
            for tag in instance.tags:
                if tag['Key'] == 'Project':
                    project_tag = tag['Value']
                    break  # Stop searching once we find the Name tag
        print(f"Project: { project_tag if project_tag else 'No Name tag found'}")
        for volume in instance.volumes.all():
            if volume.attachments[0]['Device'] == instance.root_device_name:
                print(f"Root Volume ID: {volume.id}, Size: {volume.size} GiB, State: {volume.state}, Type: {volume.volume_type}")
                break  # Only print the root volume
        print("-" * 40)

if __name__ == "__main__":
    # Specify the AWS region you want to use
    aws_region = 'us-east-1'  # Change this to your desired region
    list_ec2_instances(aws_region)
