
import re

a = 'C|C++|Java|C#|Python|Javascript'

# re.findall('pattern/正则表达式',a)
r = re.findall('Python',a)
# 规则
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')
# print(r)

# print(a.index('Python') >-1)

# print('Python' in a)