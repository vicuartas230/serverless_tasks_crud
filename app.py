#!/usr/bin/env python3
import os

import aws_cdk as cdk

from serverless_tasks_crud.serverless_tasks_crud_stack import ServerlessTasksCrudStack


app = cdk.App()
ServerlessTasksCrudStack(app, "ServerlessTasksCrudStack",
    env=cdk.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'], region=os.environ['CDK_DEFAULT_REGION']),
)

app.synth()
