# test items
#1. 5 times
# for i in range(1, 6):
#     print('Hi, Warren')
#2. 3 times
# for i in range(1, 6, 2):
#     print('Hi, Warren')
#3.  1234567
# for i in range(1, 8):
#     print(i)
#4. 01234567
# for i in range(8):
#     print(i)
#5. 2-4-6-8
#6. 10-8-6-4-2
#7. continue
#8. when the condition is not adapt

# try items
# num = int(input("Which multiplication table would you like?\n"))
# print("Here's your table:")
# for i in range(1, 11):
#     print(num, " x ", i, " = ", num*i)

# num = int(input("Which multiplication table would you like?\n"))
# print("Here's your table:")
# i = 1
# while i < 11 :
#     print(num, " x ", i, " = ", num*i)
#     i += 1

num = int(input("Which multiplication table would you like?\n"))
high = int(input("How high do you want to go?\n"))
print("Here's your table:")
i = 1
while i <= high :
    print(num, " x ", i, " = ", num*i)
    i += 1
