# i = 0
# numbers = []
#
# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

#______________加分习题
i = 0
numbers = []

def loop(num):
    for i in range(6):
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + num
        print("Numbers now: ",numbers)
        print("At the bottom i is %d" % i)

loop(10)

print("The numbers: ")

for num in numbers:
    print(num)
