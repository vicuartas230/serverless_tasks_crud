from json import dumps
from boto3 import resource
from os import environ


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def delete(event, context):
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            return {
                "statusCode": 400,
                "body": dumps({"error": "The ID has been provided incorrectly."})
            }
        taskId = event["pathParameters"]["taskId"]
        task = table.get_item(Key={"taskId": taskId})
        if "Item" not in task:
            raise Exception("Task not found.")
        table.delete_item(
            Key={"taskId": taskId}
        )
        return {
            "statusCode": 204,
        }
    except Exception as error:
        return {
            "statusCode": 400,
            "body": dumps({"error": str(error)})
        }
