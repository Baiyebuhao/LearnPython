# 数量词{}表示  {n} {n,m}

import re

a = 'python 1111java678php'

r = re.findall('[a-z]{3,6}',a)
# r = re.findall('[a-z][a-z][a-z]',a)

# 贪婪 与 非贪婪
# python默认倾向于贪婪 ，尽可能取更多

# 非贪婪 表示方法： {}?
# r = re.findall('[a-z]{3,6}?',a)
print(r)