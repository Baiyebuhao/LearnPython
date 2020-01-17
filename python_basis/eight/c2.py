"""
def funcname(parameter_list):
    pass
"""

#参数列表可以没有
#return value  none

"""
1.实现两个数字的相加
2.打印输入的参数
"""
"""
import sys
sys.setrecursionlimit(10000)  #设置递归次数
"""

def add(x,y):
    #形式参数
    result = x+y
    return result
#return表示终止，后面的语句是不会执行的
def print_code(code):
    print(code)
#不使用return，则默认返回空值，None
add(1,2)
print_code('Python')

a = add(1,2)  #实际参数
b = print_code('Python')

print(a,b)