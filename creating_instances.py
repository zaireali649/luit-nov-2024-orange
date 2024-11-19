from typing import Any  # Import Any for type hinting.
from helpers import *  # Import all helper functions. Ensure only required helpers are imported to avoid namespace clutter.

def create_instances(ec2_client: Any, ami_type: str = "linux 2023", instance_amount: int = 1) -> None:
    """
    Create EC2 instances based on the specified AMI type and instance amount.

    Args:
        ec2_client (Any): An EC2 client object used to interact with AWS EC2.
        ami_type (str): The type of AMI to use for the instances. Defaults to "linux 2023".
                        Supported values are "ubuntu", "linux 2023", and "linux 2".
        instance_amount (int): The number of instances to create. Defaults to 1.

    Returns:
        None: This function does not return a value. It creates instances and prints messages.

    Raises:
        ValueError: If an unsupported AMI type is specified.
    """
    for i in range(instance_amount):
        if ami_type.lower() == "ubuntu":
            # Call helper function to create an Ubuntu instance.
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu Instance")
        elif ami_type.lower() == "linux 2023":
            # Call helper function to create an Amazon Linux 2023 instance.
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023 Instance")
        elif ami_type.lower() == "linux 2":
            # Call helper function to create an Amazon Linux 2 instance.
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2 Instance")
        else:
            # Handle unsupported AMI types.
            print("AMI Not Supported")
            raise ValueError(f"Unsupported AMI type: {ami_type}")

# Example usage:
ec2_client = get_ec2_client()  # Retrieve an EC2 client for interacting with AWS.
create_instances(ec2_client, instance_amount=3)  # Create three instances of the default "linux 2023" type.
