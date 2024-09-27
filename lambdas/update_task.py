from json import dumps, loads
from boto3 import resource
from os import environ


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def edit(event, context):
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            return {
                "statusCode": 400,
                "body": dumps({"error": "The ID has been provided incorrectly."})
            }
        taskId = event["pathParameters"]["taskId"]
        task = loads(event["body"])
        res = table.get_item(Key={"taskId": taskId})
        if "Item" not in res:
            raise Exception("Task not found")
        table.update_item(
            Key={"taskId": taskId},
            UpdateExpression="SET #T = :t, #D = :d, #S = :s",
            ExpressionAttributeNames={
                "#T": "title",
                "#D": "description",
                "#S": "status"
            },
            ExpressionAttributeValues={
                ":t": task["title"],
                ":d": task["description"],
                ":s": task["status"]
            }
        )
        return {
            "statusCode": 201,
            "body": dumps({"message": f"Task {taskId} updated successfully"})
        }
    except Exception as error:
        return {
            "statusCode": 400,
            "body": dumps({"error": str(error)})
        }
