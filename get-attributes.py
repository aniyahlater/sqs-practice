import boto3
import requests
import json
#creating a client


sqs = boto3.client('sqs')
QueueURL = 'https://sqs.us-east-1.amazonaws.com/730335500299/MyQueue'
def delete_msg(handle):
    delete = sqs.delete_message(
    QueueURL=QueueURL,
    ReceiptHandle=response['messages'][0]['ReceiptHandle']
    )

response = sqs.get_queue_attributes(
    QueueURL=QueueURL,
    AttributeNames[
        'All'
    ]
)

print(response['Attributes']['ApproximateNumberOfMessages'])