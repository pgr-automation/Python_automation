import boto3
import csv
import datetime
import os
from io import StringIO


## Initialize clients
region='us-east-1'
cloudwatch = boto3.client('cloudwatch', region_name=region)
ec2 = boto3.client('ec2', region_name=region)
ses = boto3.client('ses', region_name=region)

## Get Metrics detials
def get_metrics(instance_id, metric_name, start_time, end_time):
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName=metric_name,
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=['Average']

    )
    return response

## Get Instance Details
def get_instance_info():
    instances_info = {}
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_name = next(
            (tag['Value'] for tag in instance.get)
            )
