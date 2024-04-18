import boto3
import requests
import json
#creating a client
sqs = boto3.client('sqs')
QueueURL = 'https://sqs.us-east-1.amazonaws.com/730335500299/MyQueue'

response = sqs.receive_message(
    QueueURL = QueueURL,
    AttributeNames=[
        'All'
    ]
)

print(response['Messages'][0]['Body'])