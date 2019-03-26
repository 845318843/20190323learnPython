
# what did you learn from this section?
# 1. 模块是硬盘的一个单独文件，内含写好的程序
# 2. def 定义好函数，另一个文件使用import 引入模块
# 3. 一个文件是一个命名空间，在同一命名空间中调用函数，
#       可以直接用函数名调用。
# 4.局部命名空间是较小的命名空间，
#       全局命名空间是较大的命名空间，
# 5.      局部变量是定义在方法中的变量，离开方法后即销毁。
#       全局变量是定义在类中的变量，程序结束后销毁。
# 6. from time import function
# 7.  import random 标准模块

# test items
# 1. 快速定位代码位置，不同的模块组合出不同的功能，提高代码重用率
# 2. def 定义好函数， 另一个文件使用import + 文件名，引入模块
# 3. import
# 4. 相当于 导入一个 函数集
# 5. method1:  from time import *    method2: import time

# try items

# 1.
# import 代码清单15_1
# 代码清单15_1.printMyName()
#
# # 2.
# from 代码清单15_1 import *
# print(c_to_f(47))

# 3.
# import random
# for itme in range(5):
#     print(random.randint(1, 20))

# 4.
import random
import time
for itme in range(10):
    print(random.random())
    time.sleep(3)