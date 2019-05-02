# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:42:46 2019

@author: AhmadBilal
"""
import requests
import pandas as pd
import xml.etree.ElementTree as ET 
import re

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

env = "https://api.cloudcheckr.com"
account_name = input("Enter account name: ")
admin_api_key = input("Enter api key: ")

api_url = env + "/api/inventory.xml/get_resources_ec2_details_v4?access_key=" + admin_api_key + "&use_account=" + account_name

r = requests.get(api_url)

xmlstring = r.text
xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
root = ET.fromstring(xmlstring)

list = []

for instance in root.findall('./Ec2Instances/Ec2InstanceV4'):
    instanceid = instance.find('InstanceId').text  
    for tag in instance.iter('ResourceTag'):
        key = tag.find('Key')
        key = key.text
        value = tag.find('Value')
        value = value.text
        
        thisdict = dict(instanceid=instanceid, tag=key, value=value)
        list.append(thisdict)
        
df = pd.DataFrame.from_dict(list)
print(df)
