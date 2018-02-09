import boto3
from botocore.exceptions import ClientError
lambda_c = boto3.client('lambda')


def create_function(name, iam_role, archive, handler='lambda_function.lambda_handler'):
    with open(archive, 'rb') as f:
        contents = f.read()
    try:
        res = lambda_c.create_function(
            FunctionName=name,
            Runtime='python2.7',
            Role=iam_role,
            Handler=handler,
            Code={
                'ZipFile': contents
            },
            Description='Lambda Function for AWS Lets-Encrypt',
            Timeout=30,
            MemorySize=128,
            Publish=True
        )
    except Exception as e:
        print(e)
        return None

    return res['FunctionArn']


def add_event_permission(name, rule_name, rule_arn):
    lambda_c.add_permission(
        FunctionName=name,
        StatementId="{0}-Event".format(rule_name),
        Action='lambda:InvokeFunction',
        Principal='events.amazonaws.com',
        SourceArn=rule_arn,
    )
