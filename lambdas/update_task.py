from json import dumps, loads
from boto3 import resource
from os import environ
from utils import create_update_expression, status_choices


dynamodb = resource("dynamodb")
table = dynamodb.Table(environ["TABLE_NAME"])


def edit(event, context):
    try:
        if len(event["pathParameters"]["taskId"]) != 36:
            statusCode = 400
            responseBody = {"error": "The ID has been provided incorrectly."}
        else:
            taskId = event["pathParameters"]["taskId"]
            res = table.get_item(Key={"taskId": taskId})
            if "Item" not in res:
                statusCode = 404
                responseBody = {"error": "Task not found"}
            else:
                task = loads(event["body"])
                if task["status"] not in status_choices:
                    return {
                        "statusCode" : 400,
                        "body": dumps({"error": "Status incorrect"})
                    }
                updateExpression = create_update_expression(task)
                table.update_item(
                    Key={"taskId": taskId},
                    UpdateExpression=updateExpression["UpdateExpression"],
                    ExpressionAttributeNames=updateExpression["ExpressionAttributeNames"],
                    ExpressionAttributeValues=updateExpression["ExpressionAttributeValues"]
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
