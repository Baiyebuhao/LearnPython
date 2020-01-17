import json

# json_str = '{"name":"qiyue","age":18,"flag":false}'
json_str = '[{"name":"qiyue","age":18,"flag":false},{"name":"qiyue","age":18}]'

#dict
# 反序列化  序列化
student = json.loads(json_str)
print(type(student))
print(student)
# print(student['name'])
# print(student['age'])