#python 导入包的第一种方式

import seven.t.c7
#导入模块
print(seven.t.c7.a)

#记住加上命名空间

#可减少长度
import seven.t.c7 as m
#导入模块
print(m.a)

#python 导入包的第二种方式
from seven.t import c7
#导入模块
print(c7.a)

#from module import a,def
from seven.t.c7 import a
#导入的具体的变量
print(a)

#导入多个变量
from seven.t.c7 import *
print(a)
print(c)
print(d)