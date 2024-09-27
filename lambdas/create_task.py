from json import loads, dumps
from boto3 import resources
from os import environ
from uuid import uuid4
from boto3.dynamodb.conditions import Attr


dynamodb = resources("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def add(event, context):
    try:
        task = loads(event["body"])
        if "title" not in task or "status" not in task:
            return {
                "statusCode": 400,
                "body": dumps({"error": "Missing required attributes."})
            }
        new_task = {
            "taskId": str(uuid4()),
            "title": task["title"],
            "description": task["description"],
            "status": task["status"]
        }
        res = table.scan(FilterExpression=Attr("title").eq(new_task["title"]))
        if res["Items"]:
            raise Exception("Task already exists.")
        table.put_item(Item=new_task)
        return {
            "statusCode": 201,
            "body": dumps({"message": f"Task {new_task['taskId']} added successfully"})
        }
    except Exception as error:
        return {
            "statusCode": 400,
            "body": dumps({"error": str(error)})
        }
