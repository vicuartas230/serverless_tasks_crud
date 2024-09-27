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

        get_task_function = _lambda.Function(self, "GetTaskFunction",
            runtime = _lambda.Runtime.PYTHON_3_9,
            handler = "get_task.fetch",
            code = _lambda.Code.from_asset("lambdas"),
            environment = {
                "TABLE_NAME": db.table_name
            }
        )

        update_task_function = _lambda.Function(self, "UpdateTaskFunction",
            runtime = _lambda.Runtime.PYTHON_3_9,
            handler = "update_task.edit",
            code = _lambda.Code.from_asset("lambdas"),
            environment = {
                "TABLE_NAME": db.table_name
            }
        )

        delete_task_function = _lambda.Function(self, "DeleteTaskFunction",
            runtime = _lambda.Runtime.PYTHON_3_9,
            handler = "delete_task.delete",
            code = _lambda.Code.from_asset("lambdas"),
            environment = {
                "TABLE_NAME": db.table_name
            }
        )

        db.grant_read_data(get_task_function)
        db.grant_read_write_data(create_task_function)
        db.grant_read_write_data(update_task_function)
        db.grant_read_write_data(delete_task_function)

        api = apigateway.RestApi(self, "APIEndpoint",
            rest_api_name = "TasksAPI",
            description = "This REST API manage CRUD operations for tasks"
        )

        tasks = api.root.add_resource("tasks")
        tasks.add_method("POST", apigateway.LambdaIntegration(create_task_function))

        task = tasks.add_resource("{taskId}")
        task.add_method("GET", apigateway.LambdaIntegration(get_task_function))
        task.add_method("PUT", apigateway.LambdaIntegration(update_task_function))
        task.add_method("DELETE", apigateway.LambdaIntegration(delete_task_function))
