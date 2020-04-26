# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='espiercyvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
from pathlib import path
pathname = r'C:\Users\Evan\Downloads\Creatures Underwater.mp4'
path = Path(pathname).expanduser().resolve()
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result.keys()
result['JobStatus']
result['Labels']
