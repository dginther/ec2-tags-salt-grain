mport os
import socket
import pprint
import boto.ec2

def ec2_roles():
	hostname = socket.gethostname()
	conn = boto.ec2.connect_to_region("us-east-1", 
		aws_access_key_id='PUTACCESSKEYHERE',
		aws_secret_access_key='PUTSECRETACCESSKEYHERE')
	reservation = conn.get_all_instances(filters={"tag:Name": hostname})[0]
	instance = reservation.instances[0]
	tags = instance.tags.get('Roles','')
	grains={}
	grains['ec2_roles'] = tags.split(',')
	return grains
