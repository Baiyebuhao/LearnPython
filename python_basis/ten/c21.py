
import json

student = [
            {"name":"qiyue","age":18,"flag":false}
            {"name":"qiyue","age":18}
          ]


json_str = json.dumps(student)
print(type(json_str))
print(json_str)

# json对象，json,json字符串