import random
die_1 = random.randint(1, 6)

sides = [1, 2, 3, 4, 5, 6]
die_1 = random.choice(sides)

two_dice = random.randint(2, 12)

# 23-1
import random

totals = [0, 0,0, 0,0, 0,0, 0,0, 0,0,0,0]

for i in range(1000):
    dice_total = random.randint(2, 12)
    totals[dice_total] += 1

# for i in range(2, 13):
#     print("total", i, "came up", totals[i], "time")


import random

totals = [0, 0,0, 0,0, 0,0, 0,0, 0,0,0,0]
for i in range(1000):
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    dice_total = die_1 + die_2
    totals[ dice_total ] += 1

# for i in range(2, 13):
#     print("total", i, "came up", totals[i], "times")


# 23-3
from random import *
coin = ["Heads", "Tails"]
heads_in_row = 0
ten_heads_in_row = 0
for i in range(2000):
    if choice(coin) == "Heads":
        heads_in_row += 1
    else:
        heads_in_row = 0

    if heads_in_row == 10:
        ten_heads_in_row += 1
        heads_in_row = 0

print("We got 10 heads in a row", ten_heads_in_row, "times.")