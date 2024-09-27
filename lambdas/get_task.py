from json import dumps
from boto3 import resource
from os import environ


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def fetch(event, context):
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            statusCode = 400
            responseBody = {"error": "The ID has been provided incorrectly."}
        else:
            taskId = event["pathParameters"]["taskId"]
            body = table.get_item(
                Key={"taskId": taskId}
            )
            if "Item" not in body:
                statusCode = 404
                responseBody = {"error": "Task not found."}
            else:
                res = body["Item"]
                statusCode = 200
                responseBody = {
                    "taskId": res["taskId"],
                    "title": res["title"],
                    "description": res["description"],
                    "status": res["status"]
                }
    except Exception as error:
        statusCode = 500
        responseBody = {"error": str(error)}
    return {
        "statusCode": statusCode,
        "body": dumps(responseBody)
    }
