import json

def handler(event, context):
  response = {
    'statusCode': 200,
    'body': json.dumps({
      'results': 'This is a public API. Anyone can call me!!'
    }),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    }
  }
  return response