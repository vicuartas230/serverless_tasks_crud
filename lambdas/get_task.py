from json import dumps
from boto3 import resource
from os import environ


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def fetch(event, context):
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            return {
                "statusCode": 400,
                "body": dumps({"error": "The ID has been provided incorrectly."})
            }
        taskId = event["pathParameters"]["taskId"]
        body = table.get_item(
            Key={"taskId": taskId}
        )
        res = body["Item"]
        return {
            "statusCode": 200,
            "body": dumps({
                "taskId": res["taskId"],
                "title": res["title"],
                "description": res["description"],
                "status": res["status"]
            })
        }
    except Exception as error:
        return {
            "statusCode": 400,
            "body": dumps({"error": str(error)})
        }
