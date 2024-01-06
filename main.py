__author__ = "Alon Shrestha"

import boto3
from botocore.config import Config
import config

retryConfig = Config(
    retries=dict(
        max_attempts=10
    )
)
sts_client = boto3.client('sts')


def getSession(assumeRole, service, sessionType, region='us-east-1'):
    session = None
    sts_response = sts_client.assume_role(
        RoleArn=assumeRole,
        RoleSessionName='aws-sts-boto3-cross-account-access',
    )
    if sessionType == "client":
        session = boto3.client(service, aws_access_key_id=sts_response['Credentials']['AccessKeyId'],
                               aws_secret_access_key=sts_response['Credentials']['SecretAccessKey'],
                               aws_session_token=sts_response['Credentials']['SessionToken'],
                               region_name=region,
                               config=retryConfig
                               )
    elif sessionType == "resource":
        session = boto3.resource(service,
                                 aws_access_key_id=sts_response['Credentials']['AccessKeyId'],
                                 aws_secret_access_key=sts_response['Credentials']['SecretAccessKey'],
                                 aws_session_token=sts_response['Credentials']['SessionToken'],
                                 region_name=region,
                                 config=retryConfig)

    return session


if __name__ == "__main__":
    for account in config.accountList:
        iamRole = config.accountConfig[account]['iamRoleArn']
        ec2Client = getSession(iamRole, "ec2", "client")
        ec2Metadata = ec2Client.describe_instances()
        print(ec2Metadata)
