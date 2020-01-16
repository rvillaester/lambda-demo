import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

dynamo_db = boto3.resource('dynamodb')
gamer_table = dynamo_db.Table('gamer')

def handler(event, context):
  queryParam = event['queryStringParameters']
  print('query param', queryParam)
  message = 'Success'
  try:
    username = queryParam.get('username')
    name = queryParam.get('name')
    
    if(not username and not name):
      result = gamer_table.scan()
    else:
      if(username and not name):
        expression = Attr('username').contains(username)
      elif (username and name):
        expression = (Attr('username').contains(username) & Attr('name').contains(name))
      elif(name and not username):
        expression = Attr('name').contains(name)
      result = gamer_table.scan(FilterExpression=expression)
      
    items = result['Items']
  except BaseException as e:
    message = str(e)

  response = {
    'statusCode': 200,
    'body': json.dumps({
      'message': message,
      'items': items
    }),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    }
  }
  return response