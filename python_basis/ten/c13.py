# 组()代表组
import re
lanuage = 'PythonC#\nJavaPHP'
lanuage2 = 'PythonC#JavaC#PHPC#'
# 4~8
r1 = re.findall('c#.{1}',lanuage, re.I)
r2 = re.findall('c#.{1}',lanuage,re.I | re.S)
r3 = re.sub('C#','GO',lanuage2,0)
lanuage2 = lanuage2.replace('C#','GO')

print(r1)
print(r2)
print(r3)
print(lanuage2)