# from sys import argv
from os.path import exists

# script, from_file, to_file = argv

from_file = "D:/BaiduNetdiskDownload/Python入门到精通共10本/敲过的python/hardway-code/test.txt"
to_file = "D:/BaiduNetdiskDownload/Python入门到精通共10本/敲过的python/hardway-code/test2.txt"

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
input_f = open(from_file)
indata = input_f.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, ctrl+c to abort")
apple = input("?")
output = open(to_file, 'w')
output.write(indata)

print("Alright, all done.")

output.close()
input_f.close()