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
        for volume in instance.volumes.all():
            print(f"  Volume ID: {volume.id}")
        print("-" * 40)

if __name__ == "__main__":
    # Specify the AWS region you want to use
    aws_region = 'us-east-1'  # Change this to your desired region
    list_ec2_instances(aws_region)
