import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.update_item(
    Key={'Name': 'Mark Wilbur', 'Email': 'markwilbur@dataengineer.cloud'},
        ExpressionAttributeValues={
            ':d': 'Finance'
        },
        UpdateExpression="set Department = :d",
    )
print(response)