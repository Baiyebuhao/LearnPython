from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


#别名
class Common():
    YELLOW = 1


print(type(VIP.GREEN.value))    # <class 'int'>
print(type(VIP.GREEN.name))     # <class 'str'>
print(type(VIP.GREEN))          # <enum 'VIP'>
print(VIP['GREEN'])             # VIP.GREEN

# 枚举类型，枚举的名字，枚举的值

for v in VIP:
    print(v)



