import boto3
import json
import re
import datetime
import os

dynamo_db = boto3.resource('dynamodb')
gamer_table = dynamo_db.Table(os.getenv('Gamer_Table'))

def add_gamer(id, payload):
  print('creating student')
  gamer_table.put_item(
    Item={
      'id': id,
      'username': payload['username'],
      'name': payload['name'],
      'email': payload['email'],
      'gender': payload['gender']
    }
  )

def handler(event, context):
  payload = json.loads(event['body'])
  print('payload', payload)
  message = 'Success'
  try:
    date_today = datetime.datetime.now();
    id = re.sub("\D", "", str(date_today))
    add_gamer(id, payload)
  except BaseException as e:
    message = str(e)

  print(message)
  response = {
    'statusCode': 200,
    'body': json.dumps({
      'message': message,
      'id': id
    }),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    }
  }
  return response