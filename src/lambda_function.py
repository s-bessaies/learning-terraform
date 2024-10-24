import json

def lambda_handler(event, context):
   print(event)
   message = 'Hello from there from Lambda!' #This is thessage

   if 'body' in event:
        # The body is usually a JSON string, so parse it
        body = json.loads(event['body'])
        
        print('POST Body:', body)
        print('param1:',body.get("param1"))

   response = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": message,
        "isBase64Encoded": False
    }

   return response
   
