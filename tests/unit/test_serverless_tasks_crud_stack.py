import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_tasks_crud.serverless_tasks_crud_stack import ServerlessTasksCrudStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_tasks_crud/serverless_tasks_crud_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessTasksCrudStack(app, "serverless-tasks-crud")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
