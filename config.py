accountList = ['Account1']

accountConfig = {
    "Account1":
        {
            "id": "123456789012",
            "iamRoleArn": "arn:aws:iam::123456789012:role/role_access_account2",
            "regionList": ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'],
        },
    "Account2":
        {
            "id": "1234567890XX",
            "iamRoleArn": "arn:aws:iam::1234567890XX:role/role_access_account2",
            "regionList": ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'],
        }
}
