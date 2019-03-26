# 16-7    语法错误
# import pygame, sys, random
# from pygame.color import THECOLORS
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255, 255, 255])
# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     color_name = random.choice(THECOLORS.keys()) #  语法错误
#     color = THECOLORS[color_name]
#     line_width = random.randint(1, 3)
#     pygame.draw.rect(screen, color, [left, top, width, height], line_width)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# # 16-8
# import pygame, sys
# import math
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for x in range(0 ,640):
#     y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
#     pygame.draw.rect(screen, [0,0,0],[x,y,1,1],1)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# 16-9
# import pygame, sys
# import math
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# plotPoints = []
# for x in range(0, 640):
#     y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
#     plotPoints.append([x,y])
# pygame.draw.lines(screen, [0,0,0],False,plotPoints,1)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
