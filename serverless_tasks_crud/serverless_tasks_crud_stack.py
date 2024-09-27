from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb
)
from constructs import Construct

class ServerlessTasksCrudStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        db = dynamodb.Table(self, "TasksTable",
            partition_key={"name": "taskId", "type": dynamodb.AttributeType.STRING},
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        create_task_function = _lambda.Function(self, "CreateTaskFunction",
            runtime = _lambda.Runtime.PYTHON_3_9,
            handler = "create_task.add",
            code = _lambda.Code.from_asset("lambdas"),
            environment = {
                "TABLE_NAME": db.table_name
            }
        )

        db.grant_read_write_data(create_task_function)

        api = apigateway.RestApi(self, "APIEndpoint",
            rest_api_name = "TasksAPI",
            description = "This REST API manage CRUD operations for tasks"
        )

        tasks = api.root.add_resource("tasks")
        tasks.add_method("POST", apigateway.LambdaIntegration(create_task_function))
