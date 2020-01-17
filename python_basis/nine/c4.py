class Student():
#一个班级里所有的学生的总数
    sum = 0
    # name = 'qiyue'  
    # age = 0
#实例方法
    def __init__(self,name,age):     #定义必须要self
        #显 胜于 隐

        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1
        # print(age)
        # print(self.name)
        # print('当前班级学生总数为：' + str(self.__class__.sum))
    def marking(self,score):
        if score < 0:
            return '不能打负分'
        self.__score = score
        print(self.name + '同学本次考试分数为：' + str(self.__score))
 
    #行为和特征    
    #实例方法
    def do_homework(self):       #self指代当前调用对象的方法
        self.do_english_homework()  #内部调用
        print('homework')
    
    def do_english_homework(self):
        print()

    @classmethod  #增加一个装饰器，定义一个类方法
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod #定义一个静态方法
    def add(x,y):
        print(Student.sum)
        print('This is a static method')


student1 = Student('石敢当',18)
student2 = Student('小鸟',18)

result = student1.marking(59)
# print(result)
student1.__score = -1  #实际上是利用python 动态 ，新建了一个score
print(student1.__dict__)
# print(student1.__score)
print(student2.__dict__)
print(student2._Student__score)
# print(student2.__score)
# student1.marking(59)
# student1.do_homework()  #外部调用
# student1.add(1,2)
# Student.add(1,2)
# student1.plus_sum()
# student2 = Student('喜小乐',19)
# Student.plus_sum()
# student3 = Student('麦晓乐',17)
# Student.plus_sum()
# print(student1.name)
# print(Student.name)
# print(student1.__dict__)
# print(Student.__dict__)
# print(Student.name)

"""
在定义的方法名字前加 __ 代表私有的，外部无法访问，构造函数除外__init__(两边都有双下划线__)
"""