import boto3
import hashlib
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'buckect1a'  # Replace with your bucket name
    
    for record in event['Records']:
        try:
            # Get the object key and version ID (if versioning is enabled)
            object_key = record['s3']['object']['key']
            version_id = record['s3'].get('object', {}).get('versionId')

            logger.info(f"Data Integrity Check: Started for object '{object_key}', version '{version_id}' in bucket '{bucket_name}'")

            # Fetch the object content
            if version_id:
                response = s3.get_object(Bucket=bucket_name, Key=object_key, VersionId=version_id)
            else:
                response = s3.get_object(Bucket=bucket_name, Key=object_key)
        
            content = response['Body'].read()
            
            # Calculate MD5 checksum of the content
            checksum = hashlib.md5(content).hexdigest()
            logger.info(f"Data Integrity Check: Checksum for object '{object_key}' is '{checksum}'")

            # Here, you could compare this checksum with a stored or expected value for validation
            # For example, log it for reference, store it in a database, or verify against an expected checksum

            logger.info(f"Data Integrity Check: Completed successfully for object '{object_key}', version '{version_id}'")

        except Exception as e:
            logger.error(f"Error during data integrity check for object '{object_key}': {str(e)}")
