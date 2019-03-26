# what did you learn from this lessen
# 1. 类的实例是对象
# 2. 属性用来描述对象的特征，方法用来描述对象的行为
# 3. 一类事物的抽象描述称为类，是事物建造的蓝图
# 4.  apple = Apple()
# 5.  前者是 初始化一个对象，后者是 重写 print方法
# 6. 同一动作在不同对象上，得到不同的反应。
# 7. 在已有类的基础上增加属性或方法
# 8. 只有函数头定义，没有函数体，同时 需要pass 声明 为代码桩

# test items
# 1. 使用 class
# 2. 属性用来描述对象的特征
# 3. 方法用来表示对象的行为
# 4. 类是同一类实例的抽象， 类是实例的蓝图，实例具有属性和方法。
# 5. 实例的引用  self
# 6. 同一动作触发不同对象时，得到不同的反应。
# 7. 继承是在已有类的基础上开发新的属性或方法

# try items
# 1.
class BankAccount:
    def __init__(self):
        self.name = "father"
        self.account = "admin007"
        self.less = 9999.9

    def CheckLess(self):
        return self.less
    def AddMoney(self, num):
        self.less += num
    def PopMoney(self, num):
        self.less -= num
    def __str__(self):
       return(self.name+self.account+str(self.less)  )

# demo = BankAccount()
# print(demo)
#
# demo.AddMoney(3)
# print(demo)
# demo.PopMoney(5)
# print(demo)

# 2.
class InterestAcount(BankAccount):
    def __init__(self):
        self.name = "father"
        self.account = "admin007"
        self.less = 9999.9

    def CheckLess(self):
        return self.less
    def AddMoney(self, num):
        self.less += num
    def PopMoney(self, num):
        self.less -= num
    def __str__(self):
       return(self.name+self.account+str(self.less)  )
    def addInterest(self):
        self.less += self.less * 0.029

demo2 = InterestAcount()
print(demo2)
demo2.addInterest()
print(demo2)