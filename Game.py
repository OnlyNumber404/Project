import turtle
import time
import random
import winsound
bullets = []
myenemey = []
worldlist = []
window = turtle.Screen()
window.setup(width=800,height=600)
window.register_shape("MAPGround1.gif")
#Player Register
window.register_shape("Up.gif")
window.register_shape("Down.gif")
window.register_shape("Right.gif")
window.register_shape("Left.gif")
#Zomby Register
window.register_shape("NormalZombyRight.gif")
window.register_shape("NormalZombyUp.gif")
window.register_shape("NormalZombyDown.gif")
window.register_shape("NormalZombyLeft.gif")
window.register_shape("NormalZomby135.gif")
window.register_shape("NormalZomby-45.gif")
window.register_shape("NormalZomby-135.gif")
window.register_shape("NormalZomby45.gif")
window.title("Zomby Apocalyps")
window.tracer(0)

#bg
background = turtle.Turtle()
background.shape("MAPGround1.gif")
background.shapesize(800,600)

#player
player = turtle.Turtle()
player.penup()
player.shape("Up.gif")
speedx = 6
speedy = 6
#Player (X,Y)

#movement player
def playerup():
    player.shape("Up.gif")
    y = player.ycor()
    y += speedy
    player.sety(y)
    print(y)

def playerdown():
    player.shape("Down.gif")
    y = player.ycor()
    y -= speedy
    player.sety(y)
    print(y)

    
def playerright():
    player.shape("Right.gif")
    x = player.xcor()
    x += speedx
    player.setx(x)
    print(x)

def playerleft():
    player.shape("Left.gif")
    x = player.xcor()
    x -= speedx
    player.setx(x)
    print(x)

#Batas Player
bataskanan_dan_kiri = 706
batas_atas_dan_bawah_ = 346
#Batas windwow player
def batasplayer():
    if player.xcor() >= bataskanan_dan_kiri:
        player.setx( bataskanan_dan_kiri - 2)
    if player.xcor() <= -bataskanan_dan_kiri:
        player.setx( -bataskanan_dan_kiri + 2)
    if player.ycor() >= batas_atas_dan_bawah_:
        player.sety( batas_atas_dan_bawah_ - 2)
    if player.ycor() <= -batas_atas_dan_bawah_:
        player.sety( - batas_atas_dan_bawah_ + 2)
# Fungsi untuk menembak
bullet_speed = 20
def shoot_bullet():
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("yellow")
    bullet.shapesize(0.1, 1)
    bullet.penup()

    if player.shape() == "Up.gif":
        bullet.goto(player.xcor() + 24.500000000000078, player.ycor() +36.60000000000025)
        bullet.setheading(90)
    elif player.shape() == "Down.gif":
        bullet.goto(player.xcor()-25.400000000000095, player.ycor() -41.40000000000032)
        bullet.setheading(270)
    elif player.shape() == "Right.gif":
        bullet.goto(player.xcor()+ 60.50000000000032 , player.ycor()-23.500000000000068)
        bullet.setheading(0)
    elif player.shape() == "Left.gif":
        bullet.goto(player.xcor()- 60.50000000000032, player.ycor()+25.500000000000068)
        bullet.setheading(180)

    bullets.append(bullet)

# #bulletright potition(41.50000000000032,-23.500000000000068)
# bulletleft potition(-36.00000000000024,25.800000000000097)
# bulletdown potition(-25.400000000000095,-41.40000000000032)
# bulletup potition(24.500000000000078,36.60000000000025)



#Zomby setup
#Normal Zomby
i = 0
while i < 5:
    jumlah = random.randint(1,5)
    for i in range(1,jumlah + 1):
        yspawn = random.randint(-706,-600)
        xspawn = random.randint(-346,-300)
        emy = turtle.Turtle()
        emy.shape("NormalZombyRight.gif")
        emy.color("White")
        # emy.shapesize(3,3)
        emy.penup()
        emy.goto (xspawn,yspawn)
        emyspeed = 0.4
        myenemey.append(emy)
        worldlist.append(emy)
        i+=1
        
#Zomby follow player
def ZombyMovement(zomby,speed):
    if zomby.xcor() < player.xcor() :
        zomby.setx(zomby.xcor() + speed)
    elif zomby.xcor() > player.xcor() +5 :
        zomby.setx(zomby.xcor() - speed)
    if zomby.ycor() < player.ycor() :
        zomby.sety(zomby.ycor() + speed)
    elif zomby.ycor() > player.ycor() +5:
        zomby.sety(zomby.ycor() - speed)

#Direction Normal Zombie
def NormalZombyDirection(player, zomby):
    differencesX = zomby.xcor() - player.xcor()
    differencesY = zomby.ycor() - player.ycor()

    maxTreshold = 15
    minTreshold = 5

    if abs(differencesX) < maxTreshold and differencesY > minTreshold:
        return "NormalZombyUp.gif" # Up
    elif abs(differencesX) < maxTreshold and differencesY < minTreshold:
        return "NormalZombyDown.gif" # Down
    elif abs(differencesY) < maxTreshold and differencesX > minTreshold:
        return "NormalZombyRight.gif" # Right
    elif abs(differencesY) < maxTreshold and differencesX < minTreshold:
        return "NormalZombyLeft.gif" # Left
    elif differencesY > minTreshold and differencesX < maxTreshold:
        return "NormalZomby-135.gif" # Up Left
    elif differencesY > minTreshold and differencesX > minTreshold:
        return "NormalZomby-45.gif" # Up Right
    elif differencesY < maxTreshold and differencesX > minTreshold:
        return "NormalZomby45.gif" # Down Right
    elif differencesY < maxTreshold and differencesX < maxTreshold:
        return "NormalZomby135.gif" # Down Left

    # if emy.xcor() > player.xcor() and emy.ycor() > player.ycor():
    #     emy.shape("NormalZomby135.gif")
    # elif emy.xcor() < player.xcor() and emy.ycor() < player.ycor():
    #     emy.shape("NormalZomby-45.gif")
    # elif emy.xcor() > player.xcor() and emy.ycor() < player.ycor():
    #     emy.shape("NormalZomby-135.gif")
    # elif emy.xcor() < player.xcor() and emy.ycor() > player.ycor():
    #     emy.shape("NormalZomby45.gif")
    # elif emy.xcor() < player.xcor() and emy.ycor()==player.ycor():
    #     emy.shape("NormalZombyRight.gif")
    # elif emy.xcor() > player.xcor() and emy.ycor()==player.ycor():
    #     emy.shape("NormalZombyLeft.gif")
    # elif emy.ycor() < player.ycor() and emy.xcor()==player.xcor():
    #     emy.shape("NormalZombyUp.gif")
    # elif emy.ycor() > player.ycor() and emy.xcor()==player.xcor():
    #     emy.shape("NormalZombyDown.gif")

def getCollision(charObject : turtle, targetObject : turtle, magnitudeRange : int):
    return abs(charObject.xcor() - targetObject.xcor()) < magnitudeRange and abs(charObject.ycor() - targetObject.ycor()) < magnitudeRange

def doCollisionPush(charObject, collidingObject, knockbackMultiplier):
    eDirectionX = (charObject.xcor() - collidingObject.xcor())
    eDirectionY = (charObject.ycor() - collidingObject.ycor())
    pDirectionX = (collidingObject.xcor() - charObject.xcor())
    pDirectionY = (collidingObject.ycor() - charObject.ycor())

    charObject.setx(charObject.xcor() - ((pDirectionX - eDirectionX) * (0.0075 + knockbackMultiplier)))          
    charObject.sety(charObject.ycor() - ((pDirectionY - eDirectionY) * (0.0075 + knockbackMultiplier)))

# #Bullet Control
# def bulletup():
#     y = Shot.ycor()
#     y+= 0.1
#     Shot.sety(y)
#     print(y)

# def bulletdown():
#     y = Shot.ycor()
#     y-= 0.1
#     Shot.sety(y)
#     print(y)

# def bulletright():
#     x = Shot.xcor()
#     x+= 0.1
#     Shot.setx(x)
#     print(x)

# def bulletleft():
#     x = Shot.xcor()
#     x-= 0.1
#     Shot.setx(x)
#     print(x)

#Player clik
window.listen()
window.onkeypress(shoot_bullet, "space")
window.onkeypress(playerup,"Up")
window.onkeypress(playerdown,"Down")
window.onkeypress(playerright,"Right")
window.onkeypress(playerleft,"Left")

# #Bullet Clik
# window.onkeypress(bulletup,"w")
# window.onkeypress(bulletdown,"s")
# window.onkeypress(bulletright,"d")
# window.onkeypress(bulletleft,"a")
while True:
    for emy in myenemey:
        for obj in worldlist:
            if getCollision(emy,obj,58):
                doCollisionPush(emy,obj,0.001)
        emy.shape(NormalZombyDirection(emy,player))
        ZombyMovement(emy,emyspeed)
    for bullet in bullets[:]:
        bullet.forward(bullet_speed)
        if bullet.xcor() > 800 or bullet.xcor() < -800 or bullet.ycor() > 600 or bullet.ycor() < -600:
            bullet.hideturtle()
            bullets.remove(bullet)

    window.update()
    batasplayer()
    time.sleep(0.01)