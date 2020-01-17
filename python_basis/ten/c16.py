import re

s = 'A83C721D8E67'

r = re.match('\d',s)   #从首字母开始匹配，一旦首字母不符合，返回None
print(r)
r1 = re.search('\d',s) #搜索整个字符串，返回满足条件的结果
print(r1)
print(r1.group())

r2 = re.findall('\d',s)
print(r2)