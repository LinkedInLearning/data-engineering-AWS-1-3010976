import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

# Create item with Name: Mark Wilbur and Email: markwilbur@dataengineer.cloud

response = table.<provide method here>(
Item = { 
     'Name': <provide name here>,
     'Email': <provide email here>,
	 'Department': 'IT'
       }
)
print(response)