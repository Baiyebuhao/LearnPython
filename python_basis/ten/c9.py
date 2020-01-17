# 边界匹配 前面加^,后面加$
import re
qq = '1000000001'
# 位数 4-8位
r1 = re.findall('^\d{4,8}$',qq)
r2 = re.findall('000',qq)
r3 = re.findall('^000',qq)
r4 = re.findall('000$',qq)
print(r1)
print(r2)
print(r3)
print(r4)