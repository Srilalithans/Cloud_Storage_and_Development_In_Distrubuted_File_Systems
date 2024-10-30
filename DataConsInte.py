import boto3
import hashlib
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'bucket1a'
    
    for record in event['Records']:
        object_key = record['s3']['object']['key']
        logger.info(f"Data Integrity Check: Started for object '{object_key}' in '{bucket_name}'")

        try:
            # Retrieve the object and compute its checksum
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            content = response['Body'].read()
            checksum = hashlib.md5(content).hexdigest()
            logger.info(f"Data Integrity Check: Checksum for object '{object_key}' is '{checksum}'")
            
            # Log additional information for auditing or comparison
            logger.info(f"Data Integrity Check: Completed successfully for object '{object_key}'")
        
        except Exception as e:
            logger.error(f"Data Integrity Error: Error accessing object '{object_key}' - {str(e)}")
