import json

def lambda_handler(event, context):
  print(event)
  print(context)
  return json.dumps({"event": event, "context": context})
