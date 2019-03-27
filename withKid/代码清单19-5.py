
#19-5
# import pygame, sys, random
#
# class MyBallClass(pygame.sprite.Sprite):
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.right = location
#         self.speed = speed
#
#     def move(self):
#         global points, score_text
#         self.rect = self.rect.move(self.speed)
#         if self.rect.left < 0 or self.rect.right > screen.get_width():
#             self.speed[0] = -self.speed[0]
#             if self.rect.top < screen.get_height():
#                 hit_wall.play()
#
#         if self.rect.top <= 0 :
#             randnum = random.random() * 2
#             if randnum < 0.6 or randnum > 1.6:  randnum = 1
#             self.speed[1] = -self.speed[1] * randnum
#             self.speed[0] =  self.speed[0] *  randnum
#             print("speed is:",self.speed)
#             points = points + 1
#             score_text = font.render(str(points), 1, (0, 0, 0))
#             get_point.play()
#
# class MyPaddleClass(pygame.sprite.Sprite):
#     def __init__(self, location=[0,0]):
#         pygame.sprite.Sprite.__init__(self)
#         image_surface = pygame.surface.Surface([100, 20])
#         image_surface.fill([0,0,0])
#         self.image = image_surface.convert()
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#
# pygame.init()
# pygame.mixer.init()
#
# pygame.mixer.music.load("bg_music.mp3")
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1)
# hit = pygame.mixer.Sound("hit_paddle.wav")
# hit.set_volume(0.4)
# new_life = pygame.mixer.Sound("new_life.wav")
# new_life.set_volume(0.5)
# splat = pygame.mixer.Sound("splat.wav")
# splat.set_volume(0.6)
# hit_wall = pygame.mixer.Sound("hit_wall.wav")
# hit_wall.set_volume(0.4)
#
# get_point = pygame.mixer.Sound("get_point.wav")
# get_point.set_volume(0.2)
# bye = pygame.mixer.Sound("game_over.wav")
# bye.set_volume(0.6)
#
#
# screen = pygame.display.set_mode([640, 480])
# clock = pygame.time.Clock()
#
# ball_speed = [12, 6]
# myBall = MyBallClass('wackyball.bmp', ball_speed, [50,50])
# ballGroup = pygame.sprite.Group(myBall)
# paddle = MyPaddleClass([270, 400])
# lives = 3
# points = 0
#
# font = pygame.font.Font(None, 50)
# score_text = font.render(str(points), 1, (0, 0, 0))
# textpos = [10, 10]
# done = False
#
# while 1:
#     clock.tick(30)
#     screen.fill([255,255,255])# 全屏幕 填成黑色
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.MOUSEMOTION:
#             paddle.rect.centerx = event.pos[0]
#     if pygame.sprite.spritecollide(paddle, ballGroup, False):# 碰撞检测
#         hit.play()
#         if  myBall.rect.bottom+(myBall.rect.top-myBall.rect.bottom)/2  < paddle.rect.top:
#             # 左上角为坐标轴，板y轴大于球y轴
#             myBall.speed[1] = -myBall.speed[1] # 改变y轴运动方向
#         else:
#             myBall.speed[0] = -myBall.speed[0]  # 改变x轴运动方向
#     myBall.move()
#
#     if not done:# 还有命（机会）玩下去
#         screen.blit(myBall.image, myBall.rect)
#         screen.blit(paddle.image, paddle.rect) #在新的位置画出板子
#         screen.blit(score_text, textpos)
#         for i in range(lives): # 画出 剩余的命（机会）
#             width = screen.get_width()
#             screen.blit(myBall.image, [width - 40 * i, 20])
#         pygame.display.flip()
#
#     if myBall.rect.top >= screen.get_rect().bottom:
#         if lives == -1:
#             continue
#         splat.play()
#         lives = lives - 1
#         myBall.speed = ball_speed = [3, 5]
#
#         # <editor-fold desc="游戏是否已经结束">
#         if lives == 0:
#             lives = lives - 1
#             pygame.time.delay(1000)
#             bye.play()
#
#             final_text1 = "Game Over"
#             final_text2 = "Your final score is: " + str(points)
#             ft1_font = pygame.font.Font(None, 70)
#             ft1_surf = font.render(final_text1, 1, (0, 0, 0))
#             ft2_font = pygame.font.Font(None, 50)
#             ft2_surf = font.render(final_text2, 1, (0, 0, 0))
#             screen.blit(ft1_surf, [screen.get_width()/2 - \
#                                    ft1_surf.get_width()/2, 100])
#
#             screen.blit(ft2_surf, [screen.get_width() / 2 - \
#                                    ft2_surf.get_width() / 2, 100])
#
#             pygame.display.flip()
#             done = True # 没命（机会）玩了
#             pygame.mixer.music.fadeout(2000)
#
#         else:
#             pygame.time.delay(2000)
#             new_life.play()
#             myBall.rect.topleft = [50, 50]
#             screen.blit(myBall.image, myBall.rect)
#             pygame.display.flip()
#             pygame.time.delay(1000)
