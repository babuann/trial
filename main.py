import os
import json
import sys
import boto3

prompt="""
You are a smart assitant so please let me know what is the best way to learn machine learning ina smartest way
"""
bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    
    
}

body=json.dumps(payload)
model_id="meta.llama3-8b-instruct-v1:0"

response=bedrock.invoke_modle(body=body,model_id=model_id,accept="application/json",content_type="application/json")
response_body=json.loads(response.get("body").read())
response_text=response_body["generation"]
print(response_text)