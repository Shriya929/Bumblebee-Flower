import pgzrun
import random
WIDTH = 497
HEIGHT = 350
x = random.randint(0,500)
y = random.randint(0,400)

score = 0
b = Actor("helikopter-removebg-preview")
f = Actor("gift")

b.x = 80
b.y = 35

f.x = x
f.y = y
def draw():
    screen.blit("backdrop",(0,0))
    b.draw()
    f.draw()
    screen.draw.text("Score =" + str(score),(370,0))
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
pgzrun.go()