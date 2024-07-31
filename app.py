#!/usr/bin/env python3
import aws_cdk as cdk
from aws_pipeline.my_pipeline_stack import MyPipelineStack
import os 

ACCOUNT_ID = os.environ["ACCOUNT_ID"]
REGION = os.environ["REGION"]

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account=ACCOUNT_ID, region=REGION)
)

app.synth()