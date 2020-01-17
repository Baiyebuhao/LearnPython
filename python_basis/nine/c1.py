# 面向对象
#有意义的面向对象的代码
#类 = 面向对象
#类？对象？
#实例化：使用类前
#尽量少用下划线_连接两个名字
#类：模版 ，最基本的作用 ：封装代码
# 类和对象：类被实例化后变成一个具体的对象（传入具体数据）
class Student():
    #定义若干个变量（这里是数据成员）
    #一个班级所有学生总数
    sum = 0
    name = ''  
    age = 0
    #类变量 ()
    def __init__(self,name,age):  #在函数下面定义一个函数要加 self
        #构造函数:让模版返回不同的对象
        #只能返回None

        #初始化对象的特征
        self.name = name
        self.age = age
        #定义 实例变量
        #print('student'):

     #行为和特征：行为要找对主体
#    def do_homework(self):
#        print('homework')

#class Printer():
##在函数下面定义一个函数要加 self
#    def print_file(self):       #打印档案对应的主体应该是打印机
#        print('name: ' + self.name)
#        print('age: ' + str(self.age))

#方法和函数的区别


# student = Student()
# #如何调用类下面的方法
# student.print_file()
#类的使用最好放在另一个模块里
"""
class StudentHomework():
    #定义若干个变量
    homework_name = ''
"""
#实例化
student1 = Student('石敢当',18)
student2 = Student('小乐',17)
print(student1.name)
print(student2.name)
print(Student.name)
# student.print_file()