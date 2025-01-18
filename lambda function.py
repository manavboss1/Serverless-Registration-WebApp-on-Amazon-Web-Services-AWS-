import json
import boto3

dynamodb = boto3.resource('dynamodb')
registration_table = dynamodb.Table('registration-table')
views_table = dynamodb.Table('serverless-web-application-on-aws')

def lambda_handler(event, context):
    # Check if the request is for registration or view count
    if 'email' in event and 'name' in event and 'phone' in event and 'password' in event:
        # Registration request
        response = registration_table.put_item(
            Item={
                'email': event['email'],
                'name': event['name'],
                'phone': event['phone'],
                'password': event['password']
            }
        )
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Registration successful'})
        }
    else:
        # View count request
        response = views_table.get_item(Key={
            'id': '0'
        })
        views = response['Item']['views']
        views += 1
        
        response = views_table.put_item(Item={
            'id': '0',
            'views': views
        })
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'views': views})
        }
