# 测试题
print("test item is here")
print(8 / 3)  # python3 与 python2 结果不一样
print(8 % 3)
print(8.0 / 3)
print(6 ** 4)
print(1.7e7)
print(4.56e-1)  # 4.56e-5 运算结果太小

# 动手试一试
print("动手试一试：")
print("第一题：")
cost = 35.27
tiny = 15e-3
avg = (cost + tiny)/3
print("1.a:  ", avg)

area = 12.5 * 16.7
cir = (12.5 + 16.7)*2
print("1.b: area is", area, "m2. circumference is", cir, "m")

print("第二题：")
F = 17
C = 5.0 / 9 * (F - 32)
print(C)

print("第三题：")
print(int(200/80), "小时", int(200 % 80)/80 * 60, "分钟")