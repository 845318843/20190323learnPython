# # 13-4
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
#
# my_price = float(input("Enter a price: "))
#
# totalPrice = calculateTax(my_price, 0.06)
# print("price = ", my_price, " Total price = ", totalPrice)

# 13-6
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
#
# my_price = float(input("Enter a price: "))
#
# totalPrice = calculateTax(my_price, 0.06)
# print("price = ", my_price, " Total price = ", totalPrice)
# print(price)

# global
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     print(my_price)
#     return total
#
# my_price = float(input("Enter a price: "))
# totalPrice = calculateTax(my_price, 0.06)
# print("price = ", my_price, " Total price = ", totalPrice)


# 13-7
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     # my_price = 10000
#     global my_price  = 10000 # ->>>>>>>>>>syntaxerror: invalid syntax
#     print(my_price)
#     return total
#
# my_price = float(input("Enter a price: "))
#
# totalPrice = calculateTax(my_price, 0.06)
# print("price = ", my_price, " Total price = ", totalPrice)
# print("my_price (outside function) = ", my_price)
