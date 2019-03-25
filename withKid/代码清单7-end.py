# test items
# my_number = 25
# if my_number < 20:
#     print('Under 20')
# else:
#     print('20 or over')

# num = 40
# if 30 < num <= 40:
#     print("yes")
# else:
#     print("no")

# keyin = input();
# if keyin == 'Q':
#     print("upper Q")
# elif keyin == 'q':
#     print("lower q")
# else:
#     print("not Q or q")

# try items
# price = int(input("what's the price?"))
# if price <= 10:
#     print("10% saving", price*0.9)
# else:
#     print("20% saving", price*0.8)


# sex = input("what's your sex?( m or  f )")
# if sex == 'm':
#     print("this time we are looking for female! bye")
# elif sex == 'f':
#     age = int(input("how old are you? "))
#     if  10 < age < 12:
#         print("you are welcome!")
#     else:
#         print("we are looking for 10-12 years old girls!bye")


# capacity = float(input("what's the capacity of your tank?"))
# percent_full = float(input("what's the percent_full of your tank?"))
# per_liter = float(input("how long is a liter can run?"))
#
# print("Size of tank:", capacity)
# print("percent full:", percent_full)
# print("km per liter:", per_liter)
#
# distance = capacity * (percent_full / 100) * per_liter
# print("You can go annother %s km" % distance)
# print("The next gas station is 200 km away")
# if distance-5 >= 200:
#     print("You can wait for the next station.")
# else:
#     print("Get gas now!")


password = input("you need to input the correct password to use the program!")
while(password != "pig"):
    password = input("wrong! you need to try again!")
print("Your're in!")