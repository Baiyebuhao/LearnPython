# 闭包 = 函数 +环境变量（函数定义时）
# 意义：保留现场，保留函数正确性
def curve_pre():
    a = 25                    #定义时的环境变量
    def curve(x):
        return a*x*x
    return curve

a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))
# f(2)
# curve(2)
# print(f(2))