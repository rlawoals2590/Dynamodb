import boto3

client = boto3.client('dynamodb',
                      region_name='ap-northeast-2')
resource = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = resource.Table("TestTable")
resp = table.scan()

items = resp['Items']
count = resp['Count']
print(items, count)

print(client.describe_table(TableName="TestTable")['Table']['ItemCount'])   # 테이블 내 전체 item의 개수