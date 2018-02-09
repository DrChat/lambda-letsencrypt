import boto3
from botocore.exceptions import ClientError
events_c = boto3.client('events')

# http://boto3.readthedocs.io/en/latest/reference/services/events.html#CloudWatchEvents.Client.put_rule
def put_rule(name, sched, desc):
    res = events_c.put_rule(Name=name, ScheduleExpression=sched, Description=desc)
    return res['RuleArn']


def put_target(name, target_arn):
    events_c.put_targets(Rule=name, Targets=[
        {
            'Id': '1',
            'Arn': target_arn,
        },
    ])
