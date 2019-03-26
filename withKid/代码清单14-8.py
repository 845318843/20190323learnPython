# 14-8
# class Triangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def getArea(self):
#         area = self.width * self.height / 2.0
#         return area
#
# class Square:
#     def __init__(self, size):
#         self.size = size
#
#     def getArea(self):
#         area = self.size * self.size
#         return area
#
# myTriangle = Triangle(4, 5)
# mySquare = Square(7)
# print(myTriangle.getArea())
# print(mySquare.getArea())


class Game_object:
    def __init__(self, name):
        self.name = name

    def pickUp(self):
        pass
        # put code here to add the object
        # to the player's collection

class Coin(Game_object):
    def __init__(self, value):
        Game_object.__init__(self)
        self.value = value

    def spend(self, buyer, seller):
        pass
        # put code here to remove the coin
        # from the buyer's more money and
        # add it to the seller's money
