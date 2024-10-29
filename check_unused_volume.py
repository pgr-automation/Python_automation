import boto3
import datetime

def check_unused_volumes():
  
  ec2 = boto3.client('ec2', region_name=region)
  
  response = ec2.describe_volumes()
  
  #print(response)
  
  availabe_volumes= []
  
  for volume in response['Volumes']:
    if not volume['Attachments'] and volume['State'] == 'available':
      volume_id = volume['VolumeId']
      creation_time = volume['CreateTime']
      size = volume['Size']
      availabe_volumes.append((volume_id, size, creation_time))
  return availabe_volumes    
  
def main():
    available_volumes = check_unused_volumes()

    if available_volumes:
        for volume_id, size, creation_time in available_volumes:
            print(f"Available EBS Volumes: {volume_id}, Size:{size},Creation Time: {creation_time}")
    else:
        print("No available EBS volumes found.")

if __name__ == "__main__":
  region = 'us-east-1'
  main()

