c = 50

def add(x,y):
    c = x + y
    print(c)
#变量的作用域
#全局变量不会因为局部变量更改
add(1,2)
print(c)