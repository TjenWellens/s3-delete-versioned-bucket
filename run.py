import boto3

BUCKET  = "ifoo-bucket"

session = boto3.Session()
s3 = session.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()