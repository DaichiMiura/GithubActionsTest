import json

def lambda_handler(event, context):
  return json.dumps({"test": "test"})
