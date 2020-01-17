from enum import Enum
from enum import IntEnum  # 限制枚举类型为数字（整型限制）
from enum import IntEnum,unique #限制标签的值不能取相同

@unique                # 装饰器
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4