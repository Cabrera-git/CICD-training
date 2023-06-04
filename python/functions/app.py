import os
import json

def lambda_handler(event, response):
    json_region = os.environ['AWS_REGION']
    return "response"