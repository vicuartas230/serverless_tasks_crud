import re
from uuid import uuid4


status_choices = [
    "pending",
    "in-progress",
    "completed"
]

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

def is_valid(uuid_code):
    if re.match(uuid_code):
        return True
    return False

a = uuid4()
print(a)
