from json import dumps, loads
from boto3 import resource
from os import environ


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def edit(event, context):
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            statusCode = 400
            responseBody = {"error": "The ID has been provided incorrectly."}
        else:
            taskId = event["pathParameters"]["taskId"]
            task = loads(event["body"])
            res = table.get_item(Key={"taskId": taskId})
            if "Item" not in res:
                statusCode = 404
                responseBody = {"error": "Task not found"}
            else:
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
                statusCode = 200
                responseBody = {"message": f"Task {taskId} updated successfully"}
    except Exception as error:
        statusCode = 500
        responseBody = {"error": str(error)}
    return {
        "statusCode": statusCode,
        "body": dumps(responseBody)
    }
