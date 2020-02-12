import json

def handler(event, context):
  response = {
    'statusCode': 200,
    'body': json.dumps({
      'results': 'This is an authenticated API. Since you see this response, it means you are authenticated user. Congrats!!'
    }),
    'headers': {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    }
  }
  return response