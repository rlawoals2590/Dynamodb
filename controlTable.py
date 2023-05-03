import boto3

client = boto3.client('dynamodb',
                      region_name='ap-northeast-2')
resource = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = resource.Table("TestTable")

# 아이템 삽입
item = {'name': 'name1112', 'att1': 'attttt'}
resp = table.put_item(Item=item)
print(resp)

# 아이템 조회
resp = table.get_item(Key={'name': 'name1112'})
print(resp['Item'])

# 아이템 삭제
resp = table.delete_item(
    Key={
        'name': 'name1112'
    }
)
print(resp)

# 데이블 삭제
table.delete()