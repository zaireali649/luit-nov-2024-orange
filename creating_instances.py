from helpers import * 

def create_instances(ec2_client, ami_type="linux 2023", instance_amount=1):
    for i in range(instance_amount):
        if ami_type.lower() == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu Instance")
        elif ami_type.lower() == "linux 2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023 Instance")
        elif ami_type.lower() == "linux 2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2 Instance")
        else:
            print("AMI Not Supported")
    
ec2_client = get_ec2_client()
create_instances(ec2_client, instance_amount=3)