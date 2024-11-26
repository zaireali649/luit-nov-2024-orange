# Import the necessary library for interacting with AWS services
import boto3

# Create an S3 client using boto3 to interact with Amazon S3
s3 = boto3.client('s3')

# Fetch the list of all S3 buckets in the account
response = s3.list_buckets()

# Extract the list of buckets from the response
buckets = response["Buckets"]

# Iterate through each bucket and print its name
for bucket in buckets:
    print(bucket["Name"])
