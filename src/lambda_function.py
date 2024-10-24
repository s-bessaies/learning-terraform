import json
import boto3

def lambda_handler(event, context):
   print(event)
   message = 'Hello from there from Lambda!' #This is thessage

   if 'body' in event:
        # The body is usually a JSON string, so parse it
        body = json.loads(event['body'])
        
        print('POST Body:', body)
        print('param1:',body.get("param1")) 
        param1 = body.get("param1")       
        config = {
            "prompt":param1,
            "max_tokens":400,
            "temperature":0.75,
            "p":0.01,
            "k":0, 
            "stop_sequences":[],
            "return_likelihoods":"NONE"
        }

        input = {
            "modelId": "cohere.command-text-v14",
            "contentType": "application/json",
            "accept": "*/*",
            "body": json.dumps(config)
        }

        bedrock = boto3.client(
                service_name='bedrock-runtime',
                region_name='us-east-1'
        )
            
        response = bedrock.invoke_model(body=input["body"],
                                            modelId=input["modelId"],
                                            accept=input["accept"],
                                            contentType=input["contentType"])
                                            
        response_body = json.loads(response['body'].read())

   response = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": response_body,
        "isBase64Encoded": False
    }

   return response
   
