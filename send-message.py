import boto3
import requests
import json
#creating a client
sqs = boto3.client('sqs')
# going to create a unique id
id = requests.get('https://ids.pods.uvarc.io').josn().get('id')
response - sqs.send_message(
    QueueURL = 'https://sqs.us-east-1.amazonaws.com/730335500299/MyQueue',
    MessageBody=id.text
    MessageAttributes={
        'Author':{
            'StringValue': 'Project X',
            'DataType': 'String'
        },

        'Flavor':{
            'StringValue': 'Cookies and Cream',
            'DataType': 'String'
        }
    }
)

print(response)


