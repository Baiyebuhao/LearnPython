from enum import Enum

#枚举下面不能有相同的标签
#不同标签名对应的值可以相同
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1   #值相等的情况，第二个标签会成为第一个标签的别名
    BLACK = 3
    RED = 4

#别名

# print(VIP.GREEN)
# 遍历时不会打印出别名
# 如果需要打印出别名，需要加__members__.items
for v in VIP:
    print(v)

for w in VIP.__members__.items():
    print(w)

for u in VIP.__members__:
    print(u)