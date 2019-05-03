import boto3

client = boto3.client(
    "ec2",
    aws_access_key_id= input("YOUR ACCESS KEY:"),
    aws_secret_access_key=input("YOUR SECRET KEY:"),
    region_name="us-east-1"
)


response = client.create_tags(
    Resources=['i-06f64a4c8815764a3', 'i-0f869a9c7d8a35b78', ], 
    Tags=[
            {
                'Key':'TEST', 
                'Value':'passed'
            },
        ]
)
