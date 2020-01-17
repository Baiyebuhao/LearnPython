import re

a = 'C0C++7Java8C#9Python6Javascript'

r1 = re.findall('\d',a)   # \d可以表示数字0-9
print(r1)

"""

'Python' 普通字符   '\d' 元字符

"""
r2 = re.findall('\D',a)   # \d可以表示数字0-9
print(r2)