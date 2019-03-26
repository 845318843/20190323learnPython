# what did you learn from this lesson?
# 1.  imort pygame,sys      pygame.init()
# 2.  use ->   while true:
# 3.  screen = pygame.display.set_mode([640, 320])
# 4.  [255,255,255]  RGB mode
# 5.  screen.blit()
# 6.  rect()-> blit() -> flip()
# 7.  speed = -speed
# 8.  when x come to the max,set x = 0

# test items
# 1. white
# 2. green
# 3. rect（）
# 4. draw.line()
# 5. 像素是图像元素，简称像素
# 6. left,top
# 7. character B
# 8. none, the propery position is between DE
# 9. blit()
# 10. rect()-> blit()->

# try items
# 1.
# import pygame
# help()
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255,255,255])
# dots = [[221, 432], [225,331],  [133, 342], [141, 310],
#         [51,230],   [74, 217],  [58, 153],  [114, 164],
#         [123, 135], [176, 190], [159, 77],  [193, 93],
#         [230, 28],  [267, 93],  [301, 77],  [284, 190],
#         [327, 135], [336, 164], [402, 153], [386, 217],
#         [409,230],  [319, 310], [327, 342], [233,331],
#         [237, 432]]
# pygame.draw.polygon(screen, [255,0,0],dots,0)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 5.  什么都没有发生？？
# import pygame
# help()
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255,255,255])
# dots = [[221, 432], [225,331],  [133, 342], [141, 310],
#         [51,230],   [74, 217],  [58, 153],  [114, 164],
#         [123, 135], [176, 190], [159, 77],  [193, 93],
#         [230, 28],  [267, 93],  [301, 77],  [284, 190],
#         [327, 135], [336, 164], [402, 153], [386, 217],
#         [409,230],  [319, 310], [327, 342], [233,331],
#         [237, 432]]
# pygame.draw.polygon(screen, [255,0,0],dots,0)
#
# while True:
#     pygame.display.flip()
#     pygame.time.delay(30)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
