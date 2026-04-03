import linode_api4
import time

API_KEY = ''

client = linode_api4.LinodeClient(API_KEY)

instance = client.linode.instance_create(
    linode_type='g6-nanode-1',     # Instance type
    region='se-sto',               # Region (Stockholm)
    image='linode/ubuntu20.04',    # Operating system image
    label='NetworkBootInstance'    # Instance name
)

instance.boot()

while instance.status != 'running':
    time.sleep(5)
    instance = client.load_instance(instance.id)

print("The Linode instance is now running and ready to be configured for network boot.")

print(f"Instance IP address: {instance.ipv4[0]}")
