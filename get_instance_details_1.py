import boto3

def list_ec2_instances(region):
    # Create an EC2 resource with the specified region
    ec2 = boto3.resource('ec2', region_name=region)

    # Retrieve all EC2 instances
    instances = ec2.instances.all()
    
    # Print header
    print("Instance ID, Instance Type, State, Public IP, Private IP, Launch Time, Name, Project, Root Volume ID, Root Volume Size (GiB), Root Volume State, Root Volume Type")
    
    # Print instance details
    for instance in instances:
        # Initialize values
        name_tag = 'No Name tag found'
        project_tag = 'No Project tag found'
        root_volume_info = 'No root volume found'

        # Fetch instance details
        if instance.tags:
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    name_tag = tag['Value']
                elif tag['Key'] == 'Project':
                    project_tag = tag['Value']

        # Find the root volume
        for volume in instance.volumes.all():
            if volume.attachments[0]['Device'] == instance.root_device_name:
                root_volume_info = f"{volume.id}, {volume.size}, {volume.state}, {volume.volume_type}"
                break  # Only print the root volume
        
        # Print instance information in a single line
        print(f"{instance.id}, {instance.instance_type}, {instance.state['Name']}, "
              f"{instance.public_ip_address}, {instance.private_ip_address}, {instance.launch_time}, "
              f"{name_tag}, {project_tag}, {root_volume_info}")

if __name__ == "__main__":
    # Specify the AWS region you want to use
    aws_region = 'us-east-1'  # Change this to your desired region
    list_ec2_instances(aws_region)
