import boto3

client = boto3.client('dynamodb',
                      region_name='ap-northeast-2')
resource = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = resource.Table("TestTable")

query = {'Key': {'name': 'name1111'},
         'UpdateExpression': 'set att1=:new_data',
         'ExpressionAttributeValues': {
             ':new_data': 'new_attttt'
         }
         }
resp = table.update_item(**query)
print(resp)