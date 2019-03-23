formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

# 加分习题  最后一行双引号部分表示变量为字符串，单引号被双引号包着，并且没有转义字符在前，就是字面的意思
#  %r内容输出（变量内容是字符串）