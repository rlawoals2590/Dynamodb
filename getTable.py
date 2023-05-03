import boto3

client = boto3.client('dynamodb',
                      region_name='ap-northeast-2')
resource = boto3.resource('dynamodb', region_name='ap-northeast-2')

table = resource.Table("TestTable")

print(table)