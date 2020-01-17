from enum import Enum
#枚举:也是一个类,但是不可更改
#意义：重在标签，不在值
#枚举下面不能有相同的标签
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

#普通类
class Common():
    YELLOW = 1


# print(VIP.GREEN.value)  # 获取枚举的值 value
#                         # 获取标签的名字 name
# print(VIP.GREEN)
print(type(VIP.GREEN.value))
print(type(VIP.GREEN))
# VIP.YELLOW = 6
# VIP.black VIP.green