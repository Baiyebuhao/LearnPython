#数字 转化成 枚举类型
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

a = 1
print(VIP(a))