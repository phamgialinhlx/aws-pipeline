#!/usr/bin/env python3
import aws_cdk as cdk
from aws_pipeline.my_pipeline_stack import MyPipelineStack
from aws_pipeline.aws_pipeline_stack import AwsPipelineStack
import os 

# ACCOUNT_ID = os.environ["ACCOUNT_ID"]
# REGION = os.environ["REGION"]

# print(f"ACCOUNT_ID: {ACCOUNT_ID}")
# print(f"REGION: {REGION}")

app = cdk.App()
# MyPipelineStack(app, "MyPipelineStack",
#     env=cdk.Environment(account=ACCOUNT_ID, region=REGION)
# )
AwsPipelineStack(app, "AwsPipelineStack")

app.synth()