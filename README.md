
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

### To use the AWS CLI to obtain your AWS account ID
1. Run the following AWS CLI command to get the AWS account ID for your `default` profile:

    ```
    aws sts get-caller-identity --query "Account" --output text
    ```

2. If you prefer to use a named profile, provide the name of your profile using the `--profile` option:

    ```
    aws sts get-caller-identity --profile your-profile-name --query "Account" --output text
    ```

### To use the AWS CLI to obtain your AWS Region
1. Run the following AWS CLI command to get the Region that you configured for your `default` profile:

    ```
    aws configure get region
    ```

2. If you prefer to use a named profile, provide the name of your profile using the `--profile` option:

    ```
    aws configure get region --profile your-profile-name
    ```

### To configure the environment for your CDK stack
1. Create the `.env` file:

    ```
    touch .env
    ```

2. Add envoriment variables:

    ```
    <KEY>=<VALUE>
    ```

## Get started with Python
To work with the AWS CDK, you must have an AWS account and credentials and have installed Node.js and the AWS CDK Toolkit. Ensure at least Node version 16.x is installed in your system

## Install the AWS CDK CLI
Use the Node Package Manager to install the CDK CLI. Install it globally is recommended using the following command:

    npm install -g aws-cdk

## Verify a successful CDK CLI installation
Run the following command to verify a successful installation. The AWS CDK CLI should output the version number:

    cdk --version

Install `CDK` package within the virtual environment

    python -m pip aws-cdk-lib

Run 


To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
