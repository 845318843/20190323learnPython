# multiplier = 5
# for i in range(1, 11):
#     print(i, "x", multiplier, "=", i * multiplier)

# 11-1
# for multiplier in range(5, 8):
#     for i in range(1, 11):
#         print(i, "x", multiplier, "=", i*multiplier)
#     print()

# 11-2
# numLines = int(input('How many lines of stars do you want? '))
# numStars = int(input('How many stars per line? '))
# for line in range(0, numLines):
#     for star in range(0, numStars):
#         print('*',end = '')
#     print()


# 11-3
# numBlocks = int(input('How many blocks of stars do you want? '))
# numLines = int(input('How many lines in each block? '))
# numStars = int(input('How many stars per line? '))
# for block in range(0, numBlocks):
#     for line in range(0, numLines):
#         for star in range(0, numStars):
#             print('*', end='')
#         print()
#     print()



# 11-4
# numBlocks = int(input('How many blocks of stars do you want? '))
# for block in range(1, numBlocks + 1):
#     for line in range(1, block * 2):
#         for star in range(1, (block + line) * 2):
#             print('*', end='')
#         print()
#     print()


# 11-5
# numBlocks = int(input('How many blocks of stars do you want? '))
# for block in range(1, numBlocks + 1):
#     print('block = ', block)
#     for line in range(1, block * 2):
#         for star in range(1, (block + line) * 2):
#             print('*', end='')
#         print(' line = ', line, 'star = ', star)
#     print()



# 11-6
# print("\tDog \tBun \tKetchup\tMustard\tOnions")
# count = 1
# for dog in [0, 1]:
#     for bun in [0, 1]:
#         for ketchup in [0, 1]:
#             for mustard in [0, 1]:
#                 for onion in [0, 1]:
#                     print('#', count, '\t', end='')
#                     print(dog, '\t', bun,\
#                           '\t', ketchup, '\t', end='')
#                     print(mustard, '\t', onion)
#                     count = count + 1


