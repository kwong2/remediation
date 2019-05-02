# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list = []

import boto3    
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])
        list.append(instance['InstanceId'])
        
#%%