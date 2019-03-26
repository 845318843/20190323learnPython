
# 12-13
letters = ['d', 'a', 'e', 'c', 'b']
# print(letters)
#
# letters.sort()
# print(letters)
#
# letters.sort()
# print(letters.sort())
#

# letters = ['d', 'a', 'e', 'c', 'b']
# letters.sort()
# print(letters)
# letters.reverse()
# print(letters)
#
# letters = ['d', 'a', 'e', 'c', 'b']
# letters.sort(reverse = True)
# print(letters)
#
#
# original_list = ['Tom', 'James', 'Sarah', 'Fred']
# new_list = original_list[:]
# new_list.sort()
# print(original_list)
# print(new_list)
#
#
# original = [5, 2, 3, 1, 4]
# newer = sorted(original)
# print(original)
# print(newer)
#
#
# my_tuple = ("red", "green", "blue")
# print(my_tuple)

# joeMarks = [55, 63, 77, 81]
# tomMarks = [65, 61, 67, 72]
# bethMarks = [97, 95, 92, 88]
#
# classMarks = [joeMarks, tomMarks, bethMarks]
# print(classMarks)

classMarks = [ [55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]
print(classMarks)

for studentMarks in classMarks:
    print(studentMarks)
print("_______")
print(classMarks[0])

print(classMarks[0][2])
