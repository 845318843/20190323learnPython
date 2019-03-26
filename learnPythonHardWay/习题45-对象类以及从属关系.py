class Animal(object):
    def eat(self):
        print("i am eat!")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    # def eat(self):
    #     print("dog eat fish!")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

Animal().eat()
Dog("pop").eat()

# plus
#1. 假定 python 的 class永远要求你加上object
#2. 子类中object位置 放 父类class
#3. 如果子类没重写eat方法，调用父类的eat
#4. 是啥规定了一类事物的特征，抽象为类，有啥是具体实现。
#5. names = ['bob','harry', 'steven']
#6. 多重继承在java中是不允许的，接口可以多继承
