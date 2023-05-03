import boto3

client = boto3.client('dynamodb',
                      region_name='ap-northeast-2')
resource = boto3.resource('dynamodb', region_name='ap-northeast-2')

schema = {
    'TableName': 'TestTable',
    'KeySchema': [
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  # Partition key
        },
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
}

retu = client.create_table(**schema)
print(retu)

print(client.list_tables())     # 테이블 목록 가져오기
print(client.describe_table(TableName="TestTable"))     # 특정 테이블 존재 여부 확인