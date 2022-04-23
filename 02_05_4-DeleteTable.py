import boto3

def delete_movie_table():

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    table.delete()

# Starts here
if __name__ == '__main__':
    delete_movie_table()
    print("Movies table deleted.")