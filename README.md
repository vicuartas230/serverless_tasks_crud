
# Welcome to the serverles tasks REST API

This is a serverless API to implement CRUD operations (Create, Read, Update, Delete) on tasks. It consists of an infrastructure built with AWS CDK to deploy a DynamoDB table `TasksTable` to store tasks, an API Gateway to manage the routes with the HTTP methods GET, POST, PUT, and DELETE, as well as, four lambda functions that handle each request.

## Prerequisites

To work with the AWS CDK, you must have an AWS account and credentials and have installed Node.js. Ensure at least Node version 16.x is installed in your system.

- **Node.js** (>= 16.x)
- **Python** (>= 3.8)
- **AWS CLI**
- **npm**
- **pip**

## Getting Started

### 1. Clone the repository

```bash
$ git clone https://github.com/vicuartas230/serverless_tasks_crud.git
$ cd serverless_tasks_crud
```

### 2. Install the AWS CDK CLI
Use the Node Package Manager to install the CDK CLI. Install it globally is recommended using the following command:

```bash
npm install -g aws-cdk
```

Run the following command to verify a successful installation. The AWS CDK CLI should output the version number:

```
cdk --version
```

### 3. Create the virtual environment
To create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```bash
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```bash
% .venv\Scripts\activate.bat
```

### 3. Install dependencies

Once the virtualenv is activated, you can install the required dependencies.


```bash
$ pip install -r requirements.txt
```

### 4. Configure your AWS environment

In this step, you configure the AWS environment for your CDK stack. By doing this, you specify which environment your CDK stack will be deployed to.

First, determine the AWS environment that you want to use. An AWS environment consists of an AWS account and AWS Region.

- #### Get your AWS account ID

    Run the following AWS CLI command to get the AWS account ID for your `default` profile:

    ```bash
    $ aws sts get-caller-identity --query "Account" --output text
    ```

    If you prefer to use a named profile, provide the name of your profile using the `--profile` option:

    ```bash
    $ aws sts get-caller-identity --profile your-profile-name --query "Account" --output text
    ```

- #### Obtain your AWS Region
    Run the following AWS CLI command to get the Region that you configured for your `default` profile:

    ```bash
    $ aws configure get region
    ```

    If you prefer to use a named profile, provide the name of your profile using the `--profile` option:

    ```bash
    $ aws configure get region --profile your-profile-name
    ```

- #### Create a `.env` file:

    ```bash
    $ touch .env
    ```

- #### Add envoriment variables:

    ```bash
    $ echo CDK_DEFAULT_ACCOUNT="your AWS account ID" >> .env
    $ echo CDK_DEFAULT_REGION="your AWS region" >> .env
    ```

### 5. Bootstrap your AWS environment

In this step, you bootstrap the AWS environment that you configured in the previous step. This prepares your environment for CDK deployments.

To bootstrap your environment, run the following from the root of your CDK project:

```bash
$ cdk bootstrap
```

### 6. Deploy your CDK stack

From the root of your project, run the following. Confirm changes if prompted:
```bash
$ cdk deploy
```

### 7. Testing your API

The URL of the endpoint will be showed once the deployment process finish. Clients like `Postman` or `curl` can be utilized to test the API.

- Create a Task

    ```bash
    $ curl -X POST https://<ENDPOINT_URL>/tasks \
        -H "Content-Type: application/json" \
        -d '{"title": "task", "description": "detailed description", "status": "pending"}'
    ```

- Get a Task

    ```bash
    $ curl -X GET https://<ENDPOINT_URL>/tasks/{<TASK_ID>}
    ```

- Update a Task

    ```bash
    $ curl -X PUT https://<ENDPOINT_URL>/tasks/{<TASK_ID>} \
        -H "Content-Type: application/json" \
        -d '{"title": "new task", "description": "new description", "status": "completed"}' 
    ```

- Delete a Task

    ```bash
    $ curl -X DELETE https://<ENDPOINT_URL>/tasks/{<TASK_ID>}
    ```

### 8. Delete your application

By deleting your application, the CloudFormation stack associated with your CDK stack including the resources created will be cleaned up avoiding unnecessary charges.

```bash
$ cdk destroy
```

## Project Structure

```
├── lambdas                             # Lambda functions for CRUD operations
│   ├── create_task.py                  # Lambda for creating a task
│   ├── get_tasks.py                    # Lambda for getting a task
│   ├── update_task.py                  # Lambda for updating a task
│   ├── delete_task.py                  # Lambda for deleting a task
│   └── utils.py                        # Functions for needed features
├── serverless_tasks_crud   
│   └── serverless_tasks_crud_stack.py  # Stack for CDK infrastructure
├── app.py                              # CDK application defining infrastructure
├── cdk.json                            # CDK project configuration
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies for Lambda functions
└── source.bat                          # Virtualenv activator on Windows
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
