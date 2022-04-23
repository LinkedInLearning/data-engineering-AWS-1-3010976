import boto3

def create_movie_table(table_name):
    
    dynamodb = boto3.client("dynamodb")
    table = dynamodb.create_table(
                                    TableName=table_name,
                                    KeySchema=[
                                        {
                                            'AttributeName': 'year',
                                            'KeyType': 'HASH'  # Partition key
                                        },
                                        {
                                            'AttributeName': 'title',
                                            'KeyType': 'RANGE'  # Sort key
                                        }
                                    ],
                                    AttributeDefinitions=[
                                        {
                                            'AttributeName': 'year',
                                            'AttributeType': 'N'
                                        },
                                        {
                                            'AttributeName': 'title',
                                            'AttributeType': 'S'
                                        },
                            
                                    ],
                                    ProvisionedThroughput={
                                        'ReadCapacityUnits': 10,
                                        'WriteCapacityUnits': 10
                                    }
                                )
    
    return table

# Create Table
table_name = "Movies"
create_movie_table(table_name=table_name)

# Status 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

print("Table status:", table.table_status)