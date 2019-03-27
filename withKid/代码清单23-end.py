import random

from card23_4 import Card

deck = []
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        deck.append(Card(suit_id, rank_id))

hand = []
for cards in range(0, 5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print("")
for card in hand:
    print(card.short_name, "=", card.long_name, " Value:", card.value)


# what did you learn
#1. 随机性是偶然性的一种形式，是具有某一概率的事件集合中
#       各个事件所表现出来的不确定性
#2. 不同的事件组合，使得概率的大小发生变化
#3. random.choice( arr[] )
#4. random.choice('head','tail')
#5. deck.remove("the one you chice")

# test items
#1. 抛硬币
#2. 前者出现2的概率为 1/11 后者为 1/36
#3. choice 和 randint()
#4. 我们定义的Card类
#5. desk数组
#6. remove()

# try item
#  6次朝上  2^6 = 1/64

