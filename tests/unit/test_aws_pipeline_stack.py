import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_pipeline.aws_pipeline_stack import AwsPipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_pipeline/aws_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsPipelineStack(app, "aws-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
