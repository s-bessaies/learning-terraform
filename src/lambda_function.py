def lambda_handler(event, context):
   print(event)
#    message = 'Hello {} !'.format(event['key1'])
   message = 'Hello from Lambda!' #This is thessage
   return {
       'message' : message
   }
