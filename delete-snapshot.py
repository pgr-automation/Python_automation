#for i in snap-0296fe484d3e84dd1 snap-09aeaf1958c314136 ; do python3 delete-snapshot.py us-east-1 $i;done
# aws ec2 describe-snapshots --region=us-east-1
import boto3
import sys
import time

region = sys.argv[1]
print(region)
delete_snap_ids = sys.argv[2]
print(delete_snap_ids)

snapshot_ids = delete_snap_ids

ec2 = boto3.client('ec2',region_name=region)

if snapshot_ids:
  for snapshot_id in [snapshot_ids]:
    print(snapshot_id)
    ec2.delete_snapshot(SnapshotId=snapshot_id)
    print(f"{snapshot_id} - is deleted")
    
    """
    while True:
      snapshot_status = ec2.describe_snapshots(SnapshotIds=[snapshot_id])
      status = snapshot_status['Snapshots'][0]['State']
      print(f"Snapshot status: {status}")
      if status == 'deleted':
            print(f"Snapshot deletion is completed for :{snapshot_id}.")
            break
      time.sleep(10)      
      """
      
else:
  print(f"Snapshot ID: {snapshot_ids}- Not found ")