#数量词
# * 匹配 0次 或者 无限多次
# + 匹配 1次 或者 无限多次
# ? 匹配 0次 或者 1次
import re

a = 'pytho0python1pythonn2'

r1 = re.findall('python*',a)
r2 = re.findall('python+',a)
r3 = re.findall('python?',a)

print(r1,r2,r3)