def lambda_handler(event, context):
   print(event)
   message = 'Hello from there from Lambda!' #This is thessage
   return {
       'message' : message
   }
