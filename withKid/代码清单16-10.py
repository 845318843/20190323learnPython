# 16-10
# import pygame, sys
# pygame.init()
#
# dots = [[221, 432], [225,331],  [133, 342], [141, 310],
#         [51,230],   [74, 217],  [58, 153],  [114, 164],
#         [123, 135], [176, 190], [159, 77],  [193, 93],
#         [230, 28],  [267, 93],  [301, 77],  [284, 190],
#         [327, 135], [336, 164], [402, 153], [386, 217],
#         [409,230],  [319, 310], [327, 342], [233,331],
#         [237, 432]]
#
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255,255,255])
# pygame.draw.lines(screen, [0, 255, 0], True, dots, 2)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 16-11
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
# my_ball = pygame.image.load("beach_ball.png")
# screen.blit(my_ball, [50,50])
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# 16-12
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
# my_ball = pygame.image.load("beach_ball.png")
# screen.blit(my_ball, [50,50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 16-13
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
# my_ball = pygame.image.load("beach_ball.png")
# screen.blit(my_ball, [50,50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.draw.rect(screen, [255,255,255],[50, 50, 90, 90], 0)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 16-14
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
# my_ball = pygame.image.load("beach_ball.png")
# x = 50
# y = 50
# screen.blit(my_ball, [x,y])
# pygame.display.flip()
# for looper in range(1, 200):
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255,255,255],[x, y, 90, 90], 0)
#     x = x + 5
#     screen.blit(my_ball, [x,y])
#     pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

