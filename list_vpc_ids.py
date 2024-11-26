# Import the necessary library for interacting with AWS services
import boto3

# Create an EC2 client to interact with the EC2 service, including VPC operations
vpc_client = boto3.client('ec2')

# Call the describe_vpcs method to retrieve information about all VPCs in the account
response = vpc_client.describe_vpcs()

# Extract the list of VPCs from the response
vpcs = response['Vpcs']

# Iterate through each VPC in the list and print its VPC ID
for vpc in vpcs:
    print(vpc['VpcId'])
