import pgzrun
import random
WIDTH = 500
HEIGHT = 400
x = random.randint(0,500)
y = random.randint(0,400)

score = 0
b = Actor("bee")
f = Actor("flower")

game_over = False

b.x = 80
b.y = 35

f.x = x
f.y = y
def draw():
    screen.blit("background",(0,0))
    b.draw()
    f.draw()
    screen.draw.text("Score =" + str(score),(370,0))
    if game_over == True:
        screen.fill("Blue")
        screen.draw.text("Times up! Your score is" + str(score),(250,200))
def timer():
    global game_over
    game_over = True
def update():
    global score
    if keyboard.left:
        b.x = b.x - 10
    if keyboard.right:
        b.x = b.x + 10
    if keyboard.down:
        b.y = b.y + 10
    if keyboard.up:
        b.y = b.y - 10
    if b.colliderect(f):
        f.x = random.randint(0,400)
        f.y = random.randint(0,400)
        score = score + 10
clock.schedule(timer,10.0)
pgzrun.go()