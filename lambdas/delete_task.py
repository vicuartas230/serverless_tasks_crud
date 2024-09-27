from json import dumps
from boto3 import resource
from os import environ


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def delete(event, context):
    responseBody = {}
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            statusCode = 400
            responseBody = {"error": "The ID has been provided incorrectly."}
        else:
            taskId = event["pathParameters"]["taskId"]
            task = table.get_item(Key={"taskId": taskId})
            if "Item" not in task:
                statusCode = 404
                responseBody = {"error": "Task not found."}
            else:
                table.delete_item(
                    Key={"taskId": taskId}
                )
                statusCode = 204
    except Exception as error:
        statusCode = 500
        responseBody = {"error": str(error)}
    return {
        "statusCode": statusCode,
        "body": dumps(responseBody)
    }
