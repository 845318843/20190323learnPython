# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# clock = pygame.time.Clock()
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         if self.rect.left <= screen.get_rect().left or \
#                      self.rect.right >= screen.get_rect().right:
#             self.speed[0] = -self.speed[0]
#         newpos = self.rect.move(self.speed)
#         self.rect = newpos
#
# my_ball = Ball('beach_ball.png', [10, 0], [20, 0])
#
# delay = 100
# interval = 50
# pygame.key.set_repeat(delay, interval)
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 my_ball.rect.top = my_ball.rect.top - 10
#             elif event.key == pygame.K_DOWN:
#                 my_ball.rect.top = my_ball.rect.top + 10
#
#     clock.tick(30)
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()




# 18.2

# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# clock = pygame.time.Clock()
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         if self.rect.left <= screen.get_rect().left or \
#                      self.rect.right >= screen.get_rect().right:
#             self.speed[0] = -self.speed[0]
#         newpos = self.rect.move(self.speed)
#         self.rect = newpos
#
# my_ball = Ball('beach_ball.png', [10, 0], [20, 0])
#
# delay = 100
# interval = 50
# pygame.key.set_repeat(delay, interval)
#
# held_down = False
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             held_down = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             held_down = False
#         elif event.type == pygame.MOUSEMOTION:
#             if held_down:
#                 my_ball.rect.center = event.pos
#
#
#     clock.tick(30)
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()

