# import pygame
# pygame.init()
# screen = pygame.display.set_mode([640, 480])


# 16-2
# import pygame
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# while True:
#     pass

# 16-3
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# 16-4
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255,255,255])
# pygame.draw.circle(screen, [255,0,0],[100,100],30,0)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()



# 16-5
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255,255,255])
# pygame.draw.circle(screen, [255,0,0],[320,240],30,0)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# 16-6
# import pygame, sys, random
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255, 255, 255])
# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     pygame.draw.rect(screen, [0, 0, 0], [left, top, width, height], 1)
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
