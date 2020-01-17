
# def curve_pre():
#     a = 25
#     def curve(x):
#         return a*x*x
#     return curve

def f1():
    a = 10
    def f2():
        # a此时将被python认为是一个局部变量
        a = 20  #如果存在此句，且此句话未引用外部变量，则这不是一个闭包
        # c = 20 * a
        print(a)
    print(a)
    f2()
    print(a)

f1()