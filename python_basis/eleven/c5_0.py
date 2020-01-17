#枚举之间的比较
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1
result = VIP.GREEN == VIP.BLACK    #可以进行等值比较
# result = VIP.GREEN > VIP.BLACK   #无法进行大小比较，直接报错
# result = VIP.GREEN is VIP.GREEN  #可以进行身份比较
print(result)