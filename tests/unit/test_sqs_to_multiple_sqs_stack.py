import aws_cdk as core
import aws_cdk.assertions as assertions

from sqs_to_multiple_sqs.sqs_to_multiple_sqs_stack import SqsToMultipleSqsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sqs_to_multiple_sqs/sqs_to_multiple_sqs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SqsToMultipleSqsStack(app, "sqs-to-multiple-sqs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
