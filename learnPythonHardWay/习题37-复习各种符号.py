# 复习关键字
and
del
from
not
while
as
# with open("/tmp/foo.txt") as file:
#     data = file.read()


elif
global
# hehe=6
# def f():
#     global hehe
#     print(hehe)
#     hehe=3
# f()
# print(hehe)


or
with
assert
# 检查条件，不符合就终止程序
# a=-1
# #报错
# assert a>0,"a超出范围"
# #正常运行
# assert a<0



else
if
pass
yield
# yield和return的关系和区别了，带yield的函数是一个生成器，而不是一个函数了，
# 这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，
# 这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，
# 生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，
# 然后遇到yield后，return出要生成的数，此步就结束。 -----csdn blog


break
except
import
print
class
exec
# 我们先读取eg.txt文件的内容，再转交exec()函数执行


in
raise
continue
finally
is
# is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同。
# 莱布尼茨说过：“世界上没有两片完全相同的叶子”，这个is正是这样的比较，
# 比较是不是同一片叶子（即比较的id是否相同，这id类似于人的身份证标识）。
# == 比较的是两个对象的内容是否相等，即内存地址可以不一样，内容一样就可以了。
# 这里比较的并非是同一片叶子，可能叶子的种类或者脉络相同就可以了。默认会调用对象的 __eq__()方法。


return
def
for


lambda
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。



try

数据类型
True
False
None
strings
numbers
floats
lists


字符串转义序列
\a
\b
\f
\n
\r
\t
\v


字符串格式化
%d
%i
%o
%u
%x
%X
%e
%E
%f
%F
%g
%G
%c
%r
%s
%%


操作符号
**
/
//
%
()
[]
{}
@
,
:
;
//=
**=