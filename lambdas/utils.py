

def create_update_expression(attrs):
    expression = {
        "UpdateExpression": "SET",
        "ExpressionAttributeNames": {},
        "ExpressionAttributeValues": {}
    }
    for k, v in attrs.items():
        expression["UpdateExpression"] += f" #{k[0].upper()} = :{k[0]},"
        expression["ExpressionAttributeNames"][f"#{k[0].upper()}"] = k
        expression["ExpressionAttributeValues"][f":{k[0]}"] = v

    expression["UpdateExpression"] = expression["UpdateExpression"][0:-1]

    return expression

exp = create_update_expression(
    {
        "title": "Finish readme file",
        "description": "To deliver the project",
        "status": "in-progress"
    }
)
