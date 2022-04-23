from decimal import Decimal
import json
import boto3


def load_data(data):
    dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('Movies')
    for item in data[:100]:
        year = int(item['year'])
        title = item['title']
        print("Adding movie:", year, title)
        table.put_item(Item=item)

# Starts Here
if __name__ == '__main__':
    with open("02_05_data.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_data(movie_list)