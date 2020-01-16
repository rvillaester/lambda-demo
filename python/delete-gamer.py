import boto3
import json

dynamo_db = boto3.resource('dynamodb')
gamer_table = dynamo_db.Table('gamer')

def handler(event, context):
  payload = json.loads(event['body'])
  print('payload', payload)
  message = 'Success'
  try:
    gamer_table.delete_item(
      Key={
        'id': payload['id']
      }
    )
  except BaseException as e:
    message = str(e)

  response = {
    'statusCode': 200,
    'body': json.dumps({
      'message': message
    }),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    }
  }
  return response