import boto3

client = boto3.client('dynamodb',
                      region_name='ap-northeast-2')
resource = boto3.resource('dynamodb', region_name='ap-northeast-2')

from boto3.dynamodb.conditions import Key  # Key

table = resource.Table("TestTable")
query = {"KeyConditionExpression": Key("name").eq("name1111")}

print(table.query(**query))     # key를 이용하여 결과를 조회
# 결과물은 readTable.py와 동일하게 table.query(**query)['Items']와 ['Count']로 각각 아이템과 아이템 수 조회 가능

from boto3.dynamodb.conditions import Attr  # Atrr

query = {"FilterExpression": Attr('att1').eq('new_attttt')}
response = table.scan(**query)  # 테이블 전체를 훑음으로 큰 테이블에서 사용하면 심각한 성능 문제가 발생할 수 있음
print(response['Items'])

# 작은 테이블이 아닌 이상 가급적 query를 쓰는 게 좋다.
# Key나 Attr에 eq뿐만 아니라 lt, gt, between 등등 많은 조건을 붙일 수 있다.

