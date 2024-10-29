# for i in i-085733c843bbee4da i-0494ad48d9fc3303c ; do python3 ebs-root-volume-backup.py us-east-1 $i;done
# aws ec2 describe-instances --region=us-east-1 --instance-id  i-085733c843bbee4da
# aws ec2 describe-instances --region=us-east-1 --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value|[0],RootDeviceName]' --output table
import boto3
import sys
import time

region = sys.argv[1]
print(region)
machine_id = sys.argv[2]

ec2 = boto3.client('ec2',region_name=region)

# Replace with your instance ID
instance_id = machine_id

# Describe the instance to get the root volume ID
response = ec2.describe_instances(InstanceIds=[instance_id])

# Extract the root volume ID
root_volume_id = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for block_device in instance['BlockDeviceMappings']:
            if block_device['DeviceName'] == instance['RootDeviceName']:
                root_volume_id = block_device['Ebs']['VolumeId']
                print(f"root volume :  {root_volume_id}")
                break

if root_volume_id:
    # Create a snapshot
    snapshot = ec2.create_snapshot(VolumeId=root_volume_id, Description=f'Snapshot of root device- {root_volume_id}')
    snapshot_id = snapshot['SnapshotId']
    print(f"Snapshot ID: {snapshot['SnapshotId']}")
    
    while True:
        snapshot_status = ec2.describe_snapshots(SnapshotIds=[snapshot_id])
        status = snapshot_status['Snapshots'][0]['State']
        print(f"Snapshot status: {status}")
        if status == 'completed':
            print(f"Snapshot creation completed for root device:{root_volume_id} and Snapshot is : {snapshot_id}.")
            break
        time.sleep(10) 
else:
    print("Root volume ID not found.")

