# from sys import argv
#
# script, filename = argv

filename = "D:/BaiduNetdiskDownload/Python入门到精通共10本/敲过的python/hardway-code/test.txt"
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRA-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. GoodBye!")

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I' m going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally, we close it.")
target.close()