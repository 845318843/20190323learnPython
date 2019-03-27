
# what did you learn from this lesson?
#1. 使用pygame.mixer.music或 pygame.mixer.sound
#2. 使用sound("").play()
#3. 使用pygame.mixer.music.play()
#4. get_busy()
#5. object.set_volume(0.x)
#6. object.play(x)
#7. object.fadeout(x)

# test items
#1. wav,mp3,oos
#2. pygame.mixer
#3. set_volume()
#4. 也是 set_volume()
#4. fadeout()

# try items
import pygame, sys
import random
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([1,1])

pygame.time.delay(500)
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.80)

pygame.mixer.music.play(-1)

secret = random.randint(1, 100)
guess = 0
tries = 0

print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99. I'll give you 6 tries.")

while guess != secret and tries < 6:
    guess = input("What's yer guess? ")
    if guess < secret:
        print("Too low, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")
    tries = tries + 1
if guess == secret:
    print("Avast! Ye got it! Found my secret, ye did!")
else:
    print("No more guesses! Better luck next time,matey!")
    print("The secret number was", secret)

