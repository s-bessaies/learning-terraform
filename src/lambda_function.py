

def lambda_handler(event, context):
   print(event)
   message = 'Hello from there from Lambda!' #This is thessage

   response = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": message,
        "isBase64Encoded": False
    }

   return response
   
