import turtle
import time
import random
# import pygame
# pygame.mixer.init()
# bgsound = pygame.mixer.Sound("ZOMBIE.mp3")
bulet = []
mynormalzomby= []
myredzomby = []
redzombycomparison = []
nomralzombycomparison = []
window = turtle.Screen()
window.setup(width=800,height=600)
window.register_shape("MAPGround1.gif")
#Player Register
window.register_shape("Up.gif")
window.register_shape("Down.gif")
window.register_shape("Right.gif")
window.register_shape("Left.gif")
#player profile
window.register_shape("PlayerProfile.gif")
#NormalZomby Register
window.register_shape("NormalZombyRight.gif")
window.register_shape("NormalZombyUp.gif")
window.register_shape("NormalZombyDown.gif")
window.register_shape("NormalZombyLeft.gif")
window.register_shape("NormalZomby135.gif")
window.register_shape("NormalZomby-45.gif")
window.register_shape("NormalZomby-135.gif")
window.register_shape("NormalZomby45.gif")
#Red Zomby Register
window.register_shape("RedZombyUp.gif")
window.register_shape("RedZombyDown.gif")
window.register_shape("RedZombyRight.gif")
window.register_shape("RedZombyLeft.gif")
window.register_shape("RedZomby135.gif")
window.register_shape("RedZomby-135.gif")
window.register_shape("RedZomby-45.gif")
window.register_shape("RedZomby45.gif")
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
player.statuslist = {}
speedx = 6
speedy = 6
#Status Player
def reload(player, statusName, statusDuration):
    player.statuslist[statusName] = {
        "timer": 0,
        "duration": statusDuration,
    }
#Player Profile
prof = turtle.Turtle()
prof.shape("PlayerProfile.gif")
prof.penup()
prof.goto(-708,340)
# #Player profile Bg
# prof_bg = turtle.Turtle()
# prof_bg.shape("square")
# prof_bg.color("white")
# prof_bg.shapesize(3,7)
# prof_bg.penup()
# prof_bg.goto(-610,340)

#playerhp
hp = 9
bar = turtle.Turtle()
bar.shape("square")
bar.color("red")
bar.shapesize(hp,0.5)
bar.right(90)
bar.penup()
bar.goto(-570,330)
#text hp
titlehp = turtle.Turtle()
titlehp.shape("square")
titlehp.color("Black")
titlehp.hideturtle()
titlehp.penup()
titlehp.goto(-640,340)
titlehp.write("Hp",align="center",font=("Courier",24,"bold"))
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


#shoot bullet
bullet_speed = 15
def shoot_bullet():
    if "BulletCD" in player.statuslist:
        pass
    else:
        shot = turtle.Turtle()
        shot.shape("square")
        shot.color("red")
        shot.shapesize(0.1, 1)
        shot.penup()

        if player.shape() == "Up.gif":
            shot.goto(player.xcor() + 24.500000000000078, player.ycor() +60.60000000000025)
            shot.setheading(90)
        elif player.shape() == "Down.gif":
            shot.goto(player.xcor()-25.400000000000095, player.ycor() -60.40000000000032)
            shot.setheading(270)
        elif player.shape() == "Right.gif":
            shot.goto(player.xcor()+ 60.50000000000032 , player.ycor()-23.500000000000068)
            shot.setheading(0)
        elif player.shape() == "Left.gif":
            shot.goto(player.xcor()- 60.50000000000032, player.ycor()+25.500000000000068)
            shot.setheading(180)

        bulet.append(shot)
        reload(player, "BulletCD", 0.10)

# #bulletright potition(41.50000000000032,-23.500000000000068)
# bulletleft potition(-36.00000000000024,25.800000000000097)
# bulletdown potition(-25.400000000000095,-41.40000000000032)
# bulletup potition(24.500000000000078,36.60000000000025)
#Bullet Hide

#Zomby setup
#Normal Zomby
i = 0
while i < 5:
    jumlah = random.randint(5,10)
    for i in range(1,jumlah + 1):
        yspawn = random.randint(-706,-600)
        xspawn = random.randint(-346,-300)
        emy = turtle.Turtle()
        emy.attributs = {
            "hp" : random.randint(10,15)
        }
        emy.shape("NormalZombyUp.gif")
        emy.color("White")
        # emy.shapesize(3,3)
        emy.penup()
        emy.goto (xspawn,yspawn)
        emyspeed = 0.7
        mynormalzomby.append(emy)
        nomralzombycomparison.append(emy)
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
    
def RedZombyDirection(player, zomby):
    differencesX = zomby.xcor() - player.xcor()
    differencesY = zomby.ycor() - player.ycor()

    maxTreshold = 15
    minTreshold = 5

    if abs(differencesX) < maxTreshold and differencesY > minTreshold:
        return "RedZombyUp.gif" # Up
    elif abs(differencesX) < maxTreshold and differencesY < minTreshold:
        return "RedZombyDown.gif" # Down
    elif abs(differencesY) < maxTreshold and differencesX > minTreshold:
        return "RedZombyRight.gif" # Right
    elif abs(differencesY) < maxTreshold and differencesX < minTreshold:
        return "RedZombyLeft.gif" # Left
    elif differencesY > minTreshold and differencesX < maxTreshold:
        return "RedZomby-135.gif" # Up Left
    elif differencesY > minTreshold and differencesX > minTreshold:
        return "RedZomby-45.gif" # Up Right
    elif differencesY < maxTreshold and differencesX > minTreshold:
        return "RedZomby45.gif" # Down Right
    elif differencesY < maxTreshold and differencesX < maxTreshold:
        return "RedZomby135.gif" # Down Left

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
#lose
def loseText():
    lose = turtle.Turtle()
    lose.shape("square")
    lose.color("White")
    lose.hideturtle()
    lose.penup()
    lose.goto(0,0)
    lose.write("YOU DIE",align="center",font=("Courier",24,"bold"))
#win text
def winText():
    lose = turtle.Turtle()
    lose.shape("square")
    lose.color("White")
    lose.hideturtle()
    lose.penup()
    lose.goto(0,0)
    lose.write("YOU SURVIVE",align="center",font=("Courier",24,"bold"))

#Player clik
window.listen()
window.onkeypress(shoot_bullet,"space")
window.onkeypress(playerup,"Up")
window.onkeypress(playerdown,"Down")
window.onkeypress(playerright,"Right")
window.onkeypress(playerleft,"Left")

# #Bullet Clik
# window.onkeypress(bulletup,"w")
# window.onkeypress(bulletdown,"s")
# window.onkeypress(bulletright,"d")
# window.onkeypress(bulletleft,"a")
is_done = False
is_finish = False
while True:
    #wave 1 title
    titlewave = turtle.Turtle()
    titlewave.shape("square")
    titlewave.color("Black")
    titlewave.hideturtle()
    titlewave.penup()
    titlewave.goto(640,340)
    titlewave.write("Wave 1",align="center",font=("Courier",24,"bold"))
    #reload status
    for statusname in list(player.statuslist.keys()):  
        status = player.statuslist[statusname]
        if status["timer"] < status["duration"]:
            status["timer"] += 0.01
        else:
            player.statuslist.pop(statusname)
    #antar player dengan normal zomby
    for emy in mynormalzomby:
        if getCollision(player,emy,49):
            doCollisionPush(player,emy,0.001)
            bar.shapesize(hp,0.5)
            if hp == 1:
                loseText()
                bar.shapesize(0.01,0.5)
                is_finish = True
                break
            else:
                hp-=1
    #antar normal zomby
    for emy in mynormalzomby:
        for obj in nomralzombycomparison:
            if getCollision(emy,obj,50):
                doCollisionPush(emy,obj,0.01)
        emy.shape(NormalZombyDirection(emy,player))
        ZombyMovement(emy,emyspeed)
    for shot in bulet:
        shot.forward(bullet_speed)
        if shot.xcor() > 800 or shot.xcor() < -800 or shot.ycor() > 600 or shot.ycor() < -600:
            shot.hideturtle()
            bulet.remove(shot)
    #Normal Zomby with bullet
    for emy in mynormalzomby:
        for shot in bulet:
            if emy in mynormalzomby:
                if getCollision(shot,emy,30):
                    shot.hideturtle()
                    bulet.remove(shot)
                    del shot
                    emy.attributs["hp"]-=2
                    if emy.attributs["hp"]<=0:
                        emy.penup()
                        emy.hideturtle()
                        mynormalzomby.remove(emy)
                        del emy
                        normaltracker = len(mynormalzomby)
                        print(normaltracker)
                        if normaltracker == 0:
                            del nomralzombycomparison
                            #wave 2 title
                            titlewave2 = turtle.Turtle()
                            titlewave2.shape("square")
                            titlewave2.color("Black")
                            titlewave2.hideturtle()
                            titlewave2.penup()
                            titlewave2.goto(640,340)
                            titlewave2.write("Wave 2",align="center",font=("Courier",24,"bold"))
                            #red zomby
                            i = 0
                            while i < 5:
                                jumlah = random.randint(5,7)
                                for i in range(1,jumlah + 1):
                                    yspawn = random.randint(-706,-600)
                                    xspawn = random.randint(-346,-300)
                                    red = turtle.Turtle()
                                    red.attributs = {
                                        "hp" : random.randint(5,10)
                                    }
                                    red.shape("RedZombyUp.gif")
                                    red.color("White")
                                    # red.shapesize(3,3)
                                    red.penup()
                                    red.goto (xspawn,yspawn)
                                    redspeed = 3
                                    myredzomby.append(red)
                                    redzombycomparison.append(red)
                                    i+=1
    #red zomby dengan player
    for red in myredzomby:
        if getCollision(player,red,49):
            doCollisionPush(player,red,0.001)
            bar.shapesize(hp,0.5)
            if hp == 1:
                loseText()
                bar.shapesize(0.01,0.5)
                is_finish = True
                break
            else:
                hp-=1
    #antar red zomby
    for red in myredzomby:
        for obj in redzombycomparison:
            if getCollision(red,obj,50):
                doCollisionPush(red,obj,0.01)
        red.shape(RedZombyDirection(red,player))
        ZombyMovement(red,redspeed)
    for shot in bulet:
        shot.forward(bullet_speed)
        if shot.xcor() > 800 or shot.xcor() < -800 or shot.ycor() > 600 or shot.ycor() < -600:
            shot.hideturtle()
            bulet.remove(shot)
     #Red Zomby with bullet
    for red in myredzomby:
        for shot in bulet:
            if red in myredzomby:
                if getCollision(shot,red,30):
                    shot.hideturtle()
                    bulet.remove(shot)
                    red.attributs["hp"]-=1
                    if red.attributs["hp"]<=0:
                        red.penup()
                        red.hideturtle()
                        myredzomby.remove(red)
                        redtracker = len(myredzomby)
                        print(redtracker)
                        if redtracker == 0:
                            is_done = True
                            winText()
                            break
    # bgsound.set_volume(0.1)
    # bgsound.play()
    window.update() 
    batasplayer()
    time.sleep(0.01)
    if is_finish:
        window.exitonclick()
