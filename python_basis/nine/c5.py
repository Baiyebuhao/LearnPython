#继承性
from c6 import Human

class Student(Human):
    # sum = 0
    def __init__(self,school,name,age):
        self.school = school
        # Human.__init__(self,name,age)  #此处必须传入self,为什么？
        #这里用 类 调用了 实例方法，本身是不正确的，所以这里是普通的方法调用
        super(Student,self).__init__(name,age)
        #法二，用super指代Human类
        # self.__score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        super(Student,self).do_homework()
        print('english homework')

student1 = Student('人名路小学','石敢当',18)
student1.do_homework()
#子类的方法和父类的方法同名，打印的是子类的方法

# Student.do_homework(' ')# 无意义，可笑调用，多次一举（这是用类调用实例方法）
# student1.do_homework
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()