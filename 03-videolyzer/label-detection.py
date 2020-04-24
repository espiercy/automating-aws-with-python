# coding: utf-8
import boto3
session = boto3.session(profile_name='pythonAutomation')
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
s3.create_bucket(Bucket='espiercyvideolyzervideos')
s3.create_bucket(Bucket='espiercyvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='espiercyvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket
from pathlib import path
from pathlib import Path
pathname = r'C:\Users\Evan\Downloads\Creatures Underwater.mp4'
path = Path(pathname).expanduser().resolve()
path
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
job_id
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['Labels']
