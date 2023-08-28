import json
import boto3

def lambda_handler(event, context):
  ssm = boto3.client("ssm", region_name="ap-northeast-1")
  ssm_response = ssm.get_parameters(
    Names=["/miura/test"]
  )
  print(ssm_response)
  print(ssm_response["Parameters][0]["Value"]
  return json.dumps({"test": "teste"})
