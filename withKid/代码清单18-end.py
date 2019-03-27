
# what do you learn
#1. 事件 大多由用户的操作 触发,如移动鼠标
#2. 事件循环指 不断检测事件是否发生
#3. 事件发生后，程序作出的响应称为事件处理
#4. 键盘事件是按下某键触发的
#5. 鼠标事件是鼠标的动作触发的
#6. 定时器事件是 设定时间间隔执行的事件
#7. pygame.font 是pygame模块用于编辑显示文字的一个模块

# test items
#1. 程序可以响应 键盘事件 和 鼠标事件
#2. 处理事件的代码叫 事件处理
#3. 检测按键的事件类型名是 event.KEYDOWN()
#4.  event.pos
#5. pygame.USEREVENT 及 pygame.NUMEVENTS
#6. pygame.time.set_time(event_number, interval)
#7. pygame.font
#8. 生成 font， 编辑font, 渲染font(blit,flip)

# try items
#1.
# 18-5
import pygame, sys, random
# from pygame.locals import *
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.right = location
        self.speed = speed

    def move(self):
        global points, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]

        if self.rect.top <= 0 :
            randnum = random.randint(1,3)
            self.speed[1] = -self.speed[1] * randnum
            self.speed[0] =  self.speed[0] *  randnum

            points = points + 1
            score_text = font.render(str(points), 1, (0, 0, 0))

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [3, 5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])
lives = 3
points = 0

font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (0, 0, 0))
textpos = [10, 10]
done = False

while 1:
    clock.tick(30)
    screen.fill([255,255,255])# 全屏幕 填成黑色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    if pygame.sprite.spritecollide(paddle, ballGroup, False):# 碰撞检测
        if  myBall.rect.bottom+(myBall.rect.top-myBall.rect.bottom)/2  < paddle.rect.top:
            # 左上角为坐标轴，板y轴大于球y轴
            myBall.speed[1] = -myBall.speed[1] # 改变y轴运动方向
        else:
            myBall.speed[0] = -myBall.speed[0]  # 改变x轴运动方向
    myBall.move()

    if not done:# 还有命（机会）玩下去
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect) #在新的位置画出板子
        screen.blit(score_text, textpos)
        for i in range(lives): # 画出 剩余的命（机会）
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        lives = lives - 1
        myBall.speed = ball_speed = [3, 5]

        # <editor-fold desc="游戏是否已经结束">
        if lives == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width()/2 - \
                                   ft1_surf.get_width()/2, 100])

            screen.blit(ft2_surf, [screen.get_width() / 2 - \
                                   ft2_surf.get_width() / 2, 100])

            pygame.display.flip()
            done = True # 没命（机会）玩了
        else:
            pygame.time.delay(2000)
            myBall.rect.topleft = [50, 50]
