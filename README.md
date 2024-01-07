## AWS STS Multiple Cross-Account Access Generator Using Boto3

This script provides a simple Python tool (`main.py`) for accessing AWS resources in multiple accounts using AWS Security Token Service (STS) to assume cross-account roles. The tool utilizes the `boto3` library and includes configurations in the `config.py` file.

### Prerequisites

Before using the script, make sure you have set up the necessary IAM roles in your source and destination AWS accounts to allow cross-account access. Follow these URLs to create an IAM role for assuming in the destination account:
- [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)
- [IAM tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

Ensure that you have the required Python libraries installed by running:

```bash
pip install -r requirements.txt
```

### Configuration

#### `config.py`

Edit the `config.py` file to include details about your AWS accounts and the roles you want to assume. Here is a sample configuration:

```python
accountList = ['Account1']

accountConfig = {
    "Account1": {
        "id": "123456789012",
        "iamRoleArn": "arn:aws:iam::123456789012:role/role_access_account2",
        "regionList": ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'],
    },
    "Account2": {
        "id": "1234567890XX",
        "iamRoleArn": "arn:aws:iam::1234567890XX:role/role_access_account2",
        "regionList": ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'],
    }
}
```

Make sure to replace the placeholder values with your actual AWS account IDs, IAM role ARNs, and region lists.

### Usage

#### Running the Script

Execute the `main.py` script to assume roles and access resources in the specified AWS accounts. The script will loop through the configured accounts and print information about EC2 instances:

```bash
python3 main.py
```

### Notes

- The script assumes the role specified in the `iamRoleArn` for each account.
- AWS region defaults to 'us-east-1' but can be configured for each account in `accountConfig`.
- The script uses AWS SDK's `boto3` library, version 1.34.14.

### Dependencies

- [boto3](https://pypi.org/project/boto3/) - AWS SDK for Python
- [botocore](https://pypi.org/project/botocore/) - Low-level, data-driven core of boto3

### License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

### Usage Disclaimer and Considerations

- This tool is a basic example and may need modifications based on specific use cases or security considerations.
- Refer to the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for more information on AWS SDK for Python.
- **Important**: Do not deploy this script in a production environment without thorough testing. Always ensure that the script meets your specific requirements and does not cause any unintended consequences.