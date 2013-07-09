ec2-tags-salt-grain
===================

Making a salt grain from EC2 tags

This grain allows you to use EC2 tags to define an ec2_roles grain on your minions programmatically.

Usage: 

Replace the AWS credentials with your valid credentials.

Replace the region with your region

Tag your EC2 Instances with a 'Roles' tag containing your roles, comma separated.

Place this grain in your <file_roots>/_grains folder.
