# # things = ['a', 'b', 'c', 'd']
# # print(things[1])
# #
# # things[1] = 'z'
# # print(things[1])
# #
# # print(things)
#
# stuff = {'name': 'Zed','age': 36,'height':6*12+2}
# # print(stuff['name'])
# #
# # print(stuff['age'])
# #
# # print(stuff['height'])
# #
# stuff['city'] = "San Francisco"
# #
# # print(stuff['city'])
#
# stuff[1] = "Wow"
#
# stuff[2] = "Neato"
#
# # print(stuff[1])
# #
# # print(stuff[2])
#
# print(stuff)
#
# del stuff['city']
# del stuff[1]
# del stuff[2]
#
# print(stuff)
#
# cities = {'CA':'San Francisco','MI':'Detroit',
#           'FL':'Jacksonville'}
#
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
#
# def find_city(themap, state):
#     if state in themap:
#         return themap[state]
#     else:
#         return "Not found."
#
# cities['_find'] = find_city
#
# while True:
#     print("State? (ENTER to quit)", end='')
#     state = input(">")
#     if not state:break
#
#     city_found = cities['_find'](cities, state)
#     print(city_found)

stuff = {'name': 'Zed','age': 36,'height':6*12+2}

print(stuff)
for item in stuff:
    print(item,end = ' ')

stuff = {'name': 'Zed','age': 36,'height':6*12+2}

for item in stuff.items():
    print(item, end = ' ')