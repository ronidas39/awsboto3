import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("totaltechnology1")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint':'eu-central-1'
    },
    
)

print(response)