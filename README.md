# **Cloud Storage and Developement in Distributed File Systems**

Welcome to the Implementation Overview for the Term Paper on TDC
Here, we’ll explain the steps used to implement various innovations in distributed cloud storage as outlined in the Term Paper:

1. ### **Storage Scalability**
-i) In the AWS Management Console, select Services and navigate to S3.                       
-ii) Select Buckets and click on Create bucket. Choose a name for your bucket (e.g., scalable-bucket), select the region, and configure the settings as needed. Leave Block Public Access settings checked if this bucket doesn’t need to be public.
-iii) Click Create bucket to create your storage.
-iv) After the bucket is created, go to Management and select Lifecycle rules to configure storage scalability rules.
-v) Click Create lifecycle rule, name it (e.g., Transition-to-Glacier), and set conditions for transitioning objects to a cheaper storage class, like Glacier, after a certain number of days (e.g., 30 days after the last modification).
-vi) Save the rule to automate transitioning objects between storage tiers, enabling storage scalability.

```json

"Bucket Policy":
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::buckect1a/*"
        }
    ]
}

```

2. **Fault Tolerance**
i) In the AWS Management Console, go to S3 and open the bucket created for scalable storage.
ii) Go to Properties, scroll to the Replication section, and click Create replication rule.
iii) Name the rule and enable Cross-Region Replication (CRR) to ensure data redundancy.
iv) Select a destination bucket in another region (create one if necessary), and configure permissions to allow replication.
v) In IAM Roles, choose Create a new role to allow S3 to manage replication. Save the settings to enable cross-region replication.

Setting Up Lambda Monitoring for Fault Tolerance:
Create a Lambda function (e.g., S3Monitor) in the AWS Lambda Console.
Use Node.js or Python as the runtime.
In the function code section, write a script to monitor S3 health and log any replication failures.
Add an S3 Object Created trigger to invoke the Lambda function whenever an object is added to the bucket.

Fault Tolerance.json

```json

"Records": [
    {
      "s3": {
        "bucket": {
          "name": "buckect1a"
        },
        "object": {
          "key": "image.png"
        }
      }
    }
  ]

```


3. **Data Consistency and Integrity**

i) In the S3 Console, select your bucket and go to Properties. Scroll down to Bucket Versioning and enable it. This allows tracking of multiple versions of objects, preserving data changes for consistency.
ii) Set up a Lambda function (e.g., S3ConsistencyCheck) to verify data integrity on object creation or modification.
iii) In the Lambda Console, create a new function and choose Python as the runtime.
iv) Add an S3 Object Created and Object Deleted trigger to invoke the function when an object is added or modified in the bucket.

Code for Data Consistency Check Using MD5 Checksum:
```json

{
  "Records": [
    {
      "eventVersion": "2.1",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "2024-10-30T12:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "s3": {
        "bucket": {
          "name": "buckect1a"
        },
        "object": {
          "key": "active/image.png",
          "size": 12345,
          "eTag": "abcd1234ef5678ghijkl90mn1234opqr",
          "versionId": "_Ntxl_bMXF82gYfhpmKjVvZ2LjPTclCh"
        }
      }
    }
  ]
}

```
