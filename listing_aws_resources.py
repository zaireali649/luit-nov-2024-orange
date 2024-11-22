from helpers import *
import json

def print_bucket_names(s3_client):
    bucket_names = list_buckets(s3_client)
    # pretty_bucket_names = json.dumps(bucket_names, indent=4) # one way to print
    # s_bucket_names = '\n'.join(bucket_names) # print using string manipulation
    for bucket_name in bucket_names: # iterate and print each element 
        print(bucket_name)

def print_instance_ids(ec2_client):
    instances = describe_instances(ec2_client)
    instance_ids = []
    print(type(instance_ids))
    for instance in instances:
        instance_ids.append(instance['InstanceId'])
    for instance_id in instance_ids:
        print(instance_id) 



ec2_client = get_ec2_client()
s3_client = get_s3_client()

#print_bucket_names(s3_client)
print_instance_ids(ec2_client)