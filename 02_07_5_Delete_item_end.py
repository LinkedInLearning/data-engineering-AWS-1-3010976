import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.delete_item(Key = {'Name': 'Mark Wilbur', 'Email': 'markwilbur@dataengineer.cloud'})

print(response)