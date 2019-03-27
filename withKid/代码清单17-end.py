
# # 17-4
# import sys, pygame
# from random import *
#
# class MyBallClass(pygame.sprite.Sprite):
#     def __init__(self, image_file, location, speed):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         self.rect = self.rect.move(self.speed)
#         if self.rect.left < 0 or self.rect.right > width:
#             self.speed[0] = -self.speed[0]
#
#         if self.rect.top < 0 or self.rect.bottom > height:
#             self.speed[1] = -self.speed[1]
#
# def animate(group):
#     screen.fill([255, 255, 255])
#     for ball in group:
#         ball.move()
#     for ball in group:
#         group.remove(ball)
#         if pygame.sprite.spritecollide(ball, group, False):
#             ball.speed[0] = -ball.speed[0]
#             ball.speed[1] = -ball.speed[1]
#
#         group.add(ball)
#
#         screen.blit(ball.image, ball.rect)
#     pygame.display.flip()
#     # pygame.time.delay(50)
#
# size = width, height = 640, 480
# screen = pygame.display.set_mode(size)
# screen.fill([255, 255, 255])
# img_file = "beach_ball.png"
# clock = pygame.time.Clock()
# group = pygame.sprite.Group()
# for row in range(0, 2):
#     for column in range(0, 2):
#         location = [column * 180 + 10, row * 180 + 10]
#         speed = [choice([-2,2]), choice([-2,2])]
#         ball = MyBallClass(img_file, location, speed)
#         group.add(ball)
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             frame_rate = clock.get_fps()
#             print("frame rate = ", frame_rate)
#             sys.exit()
#
#     animate(group)
#     clock.tick(30)


# what did you learn from this lesson?
#1. pygame.sprite.spritecollide()
#2. group = pygame.sprite.Group()
#3. ball.move(),group.remove(ball),group.add(ball)
#4. clock = pygame.time.Clock(),clock.tick(30)

# test items
#1. 两个动画精灵是否接触或重叠
#2. 前者是球矩阵区接触也算碰，后者必须球本身接触才算碰
#3. group
#4. time.delay(num),clock.tick(num)
#5. clock 是帧数，规定1秒内的画面数，
#   delay 是延迟，不同电脑执行相同代码耗时不同，一秒内的画面数可能不相同。
#6. clock.get_fps()

# try_items
###########
