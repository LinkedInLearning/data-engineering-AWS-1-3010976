import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

# update Department for Mark Wilbur from IT to Finance

response = table.<provide method here>(
    Key={'Name': <provide name here>, 'Email': <provide email here>},
        ExpressionAttributeValues={
            ':d': <provide new department here>
        },
        UpdateExpression="set Department = :d",
    )
print(response)