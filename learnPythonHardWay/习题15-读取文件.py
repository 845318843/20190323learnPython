#from sys import argv

#script, filename = argv
filename = "D:/BaiduNetdiskDownload/Python入门到精通共10本/敲过的python/hardway-code/test.txt"
txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())