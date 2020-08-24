# This file has 2 scripts that have to be used separately. One to start EC2 instances using Environment variables. The other is to stop EC2 instances using them
# These could be used in conjuction with CloudWatch Events to be started on a schedule say daily 9 am and closure at 6 pm.
# Python script to start instances below
import boto3
import os
import json

region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    instances=os.environ['EC2_INSTANCES'].split(",")
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
    
# Python script to start instances below
import boto3
import os
import json

region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    instances=os.environ['EC2_INSTANCES'].split(",")
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
