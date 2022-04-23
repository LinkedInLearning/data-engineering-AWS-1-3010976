import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.<provide method here>(
    Key={
        'Name': <provide name here>,
        'Email': <provide email here>
    }
)
print(response['Item'])