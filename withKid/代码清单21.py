# print('ABC\tXYZ')
# print('ABCDEFGHI\tXYZ')
#
# #21-1 打印正方形和立方体
# print("Number \tSquare \tCube")
# for i in range(1, 11):
#     print(i, '\t', i**2, i**3)
#
# print("\\")
#
# name = 'Warren Sande'
# print('My name is', name, 'and I wrote this book.')
# print('My name is %s and I wrote this book' % name)
#
# age = 13
# print('I am %i years old.' % age)
#

dec_number = 12.3456
print('It is %.2f degress today.' % dec_number)

number = 12.67
print('%i' % number)

number = 12.3456
print('% .2F' % number)

print('%+.2F' % number)

print('%e' % number)
print('%.2e' % number)

print('%E' % number)

number1 = 12.3
number2 = 456712345.6
print('%g' % number1)
print('%g' % number2)

print('I got 90% on my math test')

my_string = '%.2f' % 12.3456
print(my_string)

print("The anser is", my_string)

name_string = "Sam, Brad, Alex, Cameron"

names = name_string.split(',')
print(names)
names = name_string.split()
print(names)

word_list = ['My', 'name', 'is', 'Warren']
long_string = ' '.join(word_list)
print(long_string)

long_string = ' WOOF WOOF '.join(word_list)
print(long_string)

addr1 = '657 Maple Lane'
if 'Maple' in addr1:
    print("That address has 'Maple' in it.")
    print(addr1.index('Maple'))

name = 'Warren Sande'
short_name = name.strip('de')
print(short_name)
name = 'Warren Sande    '
short_name = name.strip()
print(short_name)
print(short_name.upper())

# what did you learn?
# \t \n
# %f %i %.2e
# split(' '),'wof'.join( arrange )
# strip('tion'),  strip()


# Test items
print("What is ",end = '')
print("your name?")

print("\n\n\n\t")
sss = 123.456
print("%e" % sss)


# try items
# name = input("name?")
# age = input("age?")
# favorite_color = input("color?")
# print(name+age+favorite_color)

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + "*" + str(i) + "=" + str(i*j) +'\t', end = ' ')
    print()

for i in range(1 , 9):
    out = i / 8.0
    print( "%.3f" % out)