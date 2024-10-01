import json
import boto3

# Replace with your EC2 region
region = 'us-east-1'

# IDs of the instances to stop in the below list
instances = ['i-027e01f865a86f009', 'i-008fb7b8912a6e622','i-07b27fdbcb705ae26']

ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: '+ str(instances))