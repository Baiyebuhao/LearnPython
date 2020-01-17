name = input("please enter your name")
s1 = float(input("请输入你的第一次成绩："))
s2 = float(input("请输入你的第二次成绩："))

if s1 >= s2:
    print("不好意思！",name,"您的成绩有所下降")
    r = (s1-s2)/s1100
    print('小明明成绩下降了%0.1f%%。' % r)
else:
    print("恭喜您！",name,"您的成绩有所上升")
    r = (s2-s1)/s1*100
    print('小明明成绩上升了%0.1f%%。' % r)