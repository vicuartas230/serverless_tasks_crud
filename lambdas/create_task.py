from json import loads, dumps
from boto3 import resource
from os import environ
from uuid import uuid4
from boto3.dynamodb.conditions import Attr


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def add(event, context):
    try:
        task = loads(event["body"])
        if "title" not in task or "status" not in task:
            statusCode = 400
            responseBody = {"error": "Missing required attributes."}
        else:
            res = table.scan(FilterExpression=Attr("title").eq(task["title"]))
            if res["Items"]:
                statusCode = 400
                responseBody = {"error": "Task already exists."}
            else:
                new_task = {
                    "taskId": str(uuid4()),
                    "title": task["title"],
                    "description": task["description"],
                    "status": task["status"]
                }
                table.put_item(Item=new_task)
                statusCode = 201
                responseBody = new_task
    except Exception as error:
        statusCode = 500
        responseBody = {"error": str(error)}
    return {
        "statusCode": statusCode,
        "body": dumps(responseBody)
    }
