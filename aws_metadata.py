import boto3

import datetime

from pprint import pprint

import time

import boto3

import json

from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

 

profile_name = '*******7619'

session = boto3.session.Session(profile_name='*******7619')

client = session.client('ec2', 'ap-south-1')

 
def create_key_pair(key_name, private_key_file_name=None):
    
    try:
        key_pair = ec2.create_key_pair(KeyName=key_name)
        logger.info("Created key %s.", key_pair.name)
        if private_key_file_name is not None:
            with open(private_key_file_name, 'w') as pk_file:
                pk_file.write(key_pair.key_material)
            logger.info("Wrote private key to %s.", private_key_file_name)
    except ClientError:
        logger.exception("Couldn't create key %s.", key_name)
        raise
    else:
        return key_pair


response = client.describe_instances()

#pprint(response)

for Instance in response['Reservations']:

    for Instances in Instance['Instances']:

        Name = "None"

        VolumeId = "None"

        PublicIpAddress = "None"

        InstanceId = Instances['InstanceId']

        VPCId = Instances['NetworkInterfaces']

        try:

           PublicIpAddress = Instances['PublicIpAddress']

        except KeyError as err:

           PublicIpAddress = "None"

        try:

            for vpc in Instances['NetworkInterfaces']:

                PrivateIP = vpc['PrivateIpAddress']

                VPCId = vpc['VpcId']

        except KeyError as err:

            print(err)        

       # PrivateIP = Instances['PrivateIpAddress']

        InstanceType = Instances['InstanceType']

        try:

            for volume in Instances['BlockDeviceMappings']:

                VolumeId = volume['Ebs']['VolumeId']

        except  KeyError as err:

            VolumeId = "None"  

        state = Instances['State']['Name']

      #  tags = Instances['Tags']

       

        try:

            for tag in Instances['Tags']:

                if tag['Key'] == 'Name':

                    Name = tag['Value']

                #    print(vpcName)

        except KeyError as ke:

            Name = "None"

        print(Name, "," ,InstanceId ,"," ,InstanceType, "," ,state,",",VPCId,",",PublicIpAddress,",",PrivateIP,",",metadata)

        