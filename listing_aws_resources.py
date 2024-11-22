from helpers import *  # Import helper functions, e.g., get_s3_client, list_buckets, describe_instances.
import json
from typing import List, Any


def print_bucket_names(s3_client: Any) -> None:
    """
    Retrieves and prints the names of all S3 buckets.

    Args:
        s3_client (Any): An AWS S3 client object for performing S3 operations.

    Returns:
        None
    """
    # Use helper function to list all buckets associated with the S3 client.
    bucket_names = list_buckets(s3_client)
    
    # Optional: Convert the bucket names to a JSON string for pretty printing.
    # pretty_bucket_names = json.dumps(bucket_names, indent=4)
    # print(pretty_bucket_names)

    # Optional: Print bucket names as a newline-separated string.
    # s_bucket_names = '\n'.join(bucket_names)
    # print(s_bucket_names)

    # Iterate over the list of bucket names and print each bucket individually.
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: Any) -> None:
    """
    Retrieves and prints the IDs of all EC2 instances.

    Args:
        ec2_client (Any): An AWS EC2 client object for performing EC2 operations.

    Returns:
        None
    """
    # Use helper function to describe instances associated with the EC2 client.
    instances = describe_instances(ec2_client)
    
    # Initialize a list to store instance IDs.
    instance_ids: List[str] = []

    # Print the type of `instance_ids` for debugging (optional).
    print(type(instance_ids))

    # Extract the 'InstanceId' from each instance and append to the list.
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    # Iterate over the list of instance IDs and print each ID.
    for instance_id in instance_ids:
        print(instance_id)


# Initialize AWS clients for EC2 and S3.
ec2_client = get_ec2_client()
s3_client = get_s3_client()

# Uncomment the following line to print S3 bucket names.
# print_bucket_names(s3_client)

# Print EC2 instance IDs.
print_instance_ids(ec2_client)
