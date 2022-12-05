import turtle
import winsound
import time
winsound.PlaySound("Music.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
screen=turtle.Screen()
screen.tracer(0)
screen.setup(width=1500,height=950)
screen.colormode(255)
screen.bgcolor(75, 132, 255)
Goombas=[]
Bricks=[]
Bricks2=[]
Questions=[]
Nothing=[]
Coins=[]
Pipes=[]
HitQuestions=[]
Mushroom=[]
triggerg=turtle.Turtle()

MarioUpLevels=0
coincount=0

Timer = turtle.Turtle()
Timer.penup()
Timer.ht()
Timer.goto(420,397)
Timer.color("white")
Time=turtle.Turtle()
Time.penup()
Time.ht()
Time.color("white")
Time.goto(395,420)
Time.write("TIME",align='left',font=('Emulogic',18,'normal'))
triggerg.penup()
triggerg.ht()
triggerg.goto(150,0)
NotMario=[Goombas, Bricks, Questions, Bricks2, [triggerg], HitQuestions, Pipes, Mushroom]
points=0
Point_counter=turtle.Turtle()
Point_counter.ht()
Point_counter.penup()
Point_counter.goto(-560,397)
Point_counter.color("white")
P_counter=turtle.Turtle()
P_counter.color("white")
P_counter.ht()
P_counter.penup()
P_counter.goto(-560,420)
P_counter.write("MARIO",align='left',font=('Emulogic',18,'normal'))

Coin_Counter=turtle.Turtle()
Coin_Counter.penup()
Coin_Counter.goto(-300,410)
turtle.register_shape('Coincounter.gif')
Coin_Counter.shape('Coincounter.gif')
Count_Coin=turtle.Turtle()
Count_Coin.ht()
Count_Coin.penup()
Count_Coin.goto(-280,397)
Count_Coin.color("white")

for i in range(11):
    coin = turtle.Turtle()
    turtle.register_shape('coinNN.gif')
    coin.shape('coinNN.gif')
    coin.penup()
    coin.hideturtle()
    coin.goto(-9000,9000)
    Coins.append(coin)
for i in range (5):
    pipe=turtle.Turtle()
    turtle.register_shape('pipe.gif')
    pipe.shape('pipe.gif')
    pipe.penup()
    Pipes.append(pipe)
for i in range(2000):
    brick = turtle.Turtle()
    turtle.register_shape('Brick.gif')
    brick.shape('Brick.gif')
    brick.penup()
    Bricks.append(brick)
for i in range(15):
    Goomba = turtle.Turtle()
    turtle.register_shape('Goomba.gif')
    Goomba.shape('Goomba.gif')
    Goomba.penup()
    Goombas.append(Goomba)
    Goomba.goto(0,9000)
for i in range(2000):
    brick2=turtle.Turtle()
    turtle.register_shape('Brick2.gif')
    brick2.shape('Brick2.gif')
    brick2.penup()
    Bricks2.append(brick2)
for i in range(13):
    question=turtle.Turtle()
    turtle.register_shape('QuestionBlock.gif')
    question.shape('QuestionBlock.gif')
    question.penup()
    Questions.append(question)
for i in range(13):
    hitquestion=turtle.Turtle()
    turtle.register_shape('HitQuestion.gif')
    hitquestion.shape('HitQuestion.gif')
    hitquestion.penup()
    hitquestion.goto(-9000,900000)
    HitQuestions.append(hitquestion)
for i in range(3):
    mushroom=turtle.Turtle()
    turtle.register_shape('mushroom.gif')
    mushroom.shape('mushroom.gif')
    mushroom.penup()
    mushroom.ht()
    mushroom.goto(-90000,9000)
    Mushroom.append(mushroom)
Mario = turtle.Turtle()
turtle.register_shape('Mario.gif')
Mario.shape('Mario.gif')
Mario.penup()


defaultMariox=-234
defaultMarioy=-344.5
defaultSpawnX=300
defaultSpawnY=-100
Mario.goto(defaultMariox, defaultMarioy)
pipeycoordinate=0
bx=-117874
b2x=-117874
by=-398
b2y=-459
for i in Bricks:
    i.goto(bx,by)
    bx+=61
for i in Bricks2:
    i.goto(b2x,b2y)
    b2x+=61
Questions[0].goto(954,-215)
Questions[1].goto(1015,-215)
Pipes[0].goto(1820,-370)
screen.update()

questionycoordinate=0
def ques_hit(que):
    quex=que.xcor()
    quey=que.ycor()
    quey+=15
    que.goto(quex,quey)
    screen.update()
def M_die():
    winsound.PlaySound("death.wav", winsound.SND_ASYNC)
    diey=0
    diey2=-50
    Mxcor = Mario.xcor()
    for i in range (10):
        diey+=4
        Mario.goto(Mxcor, diey)
        screen.update()
    Mario.write("Game Over!",align='left',font=('Emulogic',25,'normal'))
    screen.update()
    for i in range(90):
        diey2-=10
        Mario.goto(Mxcor, diey2)
        screen.update()
    screen.update()

def G_stomped(goom):
    #winsound.PlaySound("Gdeath.wav", winsound.SND_ASYNC | winsound.SND_NOSTOP)
    global points
    G_sX = goom.xcor()
    goom.goto(G_sX, -900)


def checkcollision():
    global coincount
    global points
    mushroom1 = Mushroom[1]
    for ques in Questions:
        if abs(Mario.ycor()-ques.ycor())<=30 and abs(Mario.xcor()-ques.xcor())<=41 and abs(Mario.ycor()-ques.ycor())>=10:
            ques123xcor = ques.xcor()
            ques123ycor= ques.ycor()
            index=Questions.index(ques)
            ques_hit(ques)
            if ques==Questions[0]:
                quescurentxcor=Questions[0].xcor()
                quescurentxycor=Questions[0].ycor()
                coin1=Coins[0]
                coin1.goto(quescurentxcor,quescurentxycor)
                coin1.showturtle()
                ques.ht()
                HitQuestions[index].goto(ques123xcor, ques123ycor)
                ques.goto(100000,100000)
                for i in range(6):
                    quescurentxycor+=5
                    coin1.goto(quescurentxcor,quescurentxycor)
                    screen.update()
                for i in range(3):
                    quescurentxycor-=7
                    coin1.goto(quescurentxcor,quescurentxycor)
                    screen.update()
                coin1.write("200",align='left',font=('Emulogic',10,'normal'))
                screen.update()
                coincount+=1
                points+=200
                coin1.ht()
                coin1.clear()
            elif ques==Questions[1]:
                quescurentxcor = Questions[1].xcor()
                quescurentxycor = Questions[1].ycor()
                ques.goto(10000,10000)
                ques.ht()
                HitQuestions[index].goto(ques123xcor,ques123ycor)
                screen.update()
                mushroom1.goto(quescurentxcor, quescurentxycor)
                mushroom1.showturtle()
                for i in range(7):
                    quescurentxycor += 6
                    mushroom1.goto(quescurentxcor, quescurentxycor)
                    screen.update()
            return True
def checkcolliosion2():
    for thi in HitQuestions:
        if abs(Mario.ycor()-thi.ycor())<=30 and abs(Mario.xcor()-thi.xcor())<=41 and abs(Mario.ycor()-thi.ycor())>=10:
            return True
global NextToPipe
NextToPipe=False
def checkcolliosionPipe():
    global NextToPipe
    for iht in Pipes:
        if abs(Mario.xcor()-iht.xcor())>=60 and abs(Mario.xcor()-iht.xcor())<=72 and abs(Mario.ycor()-iht.ycor())<=90:
            NextToPipe=True



            #make mario stop moving but then if no longer tuching wall then he can move.
def checkstandingQ():
    global questionycoordinate
    for qu in Questions:
        questionycoordinate = qu.ycor()
        questionycoordinate += 55
        if abs(Mario.xcor()-qu.xcor())<=50 and (Mario.ycor()-qu.ycor())<=100 and (Mario.ycor()-qu.ycor())>=0:
            return True
        else:
            return False

def checkstandingH():
    global questionycoordinate
    for qu in HitQuestions:
        questionycoordinate= qu.ycor()
        questionycoordinate+=55
        if abs(Mario.xcor()-qu.xcor()) <= 50 and (Mario.ycor()-qu.ycor())<=100 and (Mario.ycor()-qu.ycor())>=0:
            print("checkingH")
            return True
        else:
            return False, 0
def checkNotStandingQ0():
    if abs(Mario.xcor()-Questions[0].xcor())>46 and Mario.ycor()==-160:
        return True
    else:
        return False
def checkNotStandingQ1():
    if abs(Mario.xcor()-Questions[1].xcor())>46 and Mario.ycor()==-160:
        return True
    else:
        return False
def checkNotStandingH0():
    if abs(Mario.xcor()-HitQuestions[0].xcor())>46 and Mario.ycor()==-160:
        return True
    else:
        return False
def checkNotStandingH1():
    if abs(Mario.xcor()-HitQuestions[1].xcor())>46 and Mario.ycor()==-160:
        return True
    else:
        return False
def checkMNotStandingQ0():
    for i in Mushroom:
        if abs(i.xcor()-Questions[0].xcor())>46 and i.ycor()==-158.0:
            print("true1")
            return True
    else:
        return False
def checkMNotStandingQ1():
    for i in Mushroom:
        if abs(i.xcor()-Questions[1].xcor())>46 and i.ycor()==-158.0:
            print("true2")
            return True
    else:
        return False
def checkMNotStandingH0():
    for i in Mushroom:
        if abs(i.xcor()-HitQuestions[0].xcor())>46 and i.ycor()==-158.0:
            print("true3")
            return True
    else:
        return False
def checkMNotStandingH1():
    for i in Mushroom:
        print(i.ycor())
        if abs(i.xcor()-HitQuestions[1].xcor())>46 and i.ycor()==-158.0:
            print("true4")
            return True
    else:
        return False
def checkstandingP():
    global pipeycoordinate
    for qu in Pipes:
        pipeycoordinate = qu.ycor()
        pipeycoordinate += 142
        if abs(Mario.xcor()-qu.xcor())<=72 and abs(Mario.ycor()-qu.ycor())<=200 and abs(Mario.ycor()-qu.ycor())>=170:
            return True
        else:
            return False
def checkNotStandingP():
    for pi in Pipes:
        if abs(Mario.xcor()-pi.xcor())>72 and Mario.ycor()==-228:
            return True
        else:
            return False

Floor2Level=-160
def jump():
    global NextToPipe
    global MarioUpLevels
    global questionycoordinate
    curMx=Mario.xcor()
    jumpy=Mario.ycor()
    if  abs(Mario.ycor()-defaultMarioy)<=0.5:
        for u in range(16):
            jumpy+=15
            Mario.goto(curMx,jumpy)
            screen.update()
            if checkcollision()==True:
                for i in range(u+1):
                    newYPosition=Mario.ycor()-(15)
                    Mario.goto(curMx, newYPosition)
                    screen.update()
                return
            if checkcolliosion2()==True:
                for i in range(u+1):
                    newYPosition = Mario.ycor() - (15)
                    Mario.goto(curMx, newYPosition)
                    screen.update()
                return
            if checkstandingQ()==True:
                qux = Mario.xcor()
                Mario.goto(qux,questionycoordinate)
                screen.update()
                MarioUpLevels+=1
                return
            if checkstandingH()==True:
                qux = Mario.xcor()
                Mario.goto(qux,questionycoordinate)
                screen.update()
                MarioUpLevels+=1
                return
            if checkstandingP()==True:
                qux = Mario.xcor()
                Mario.goto(qux, pipeycoordinate)
                screen.update()
                MarioUpLevels += 1
                return
        if NextToPipe==True:
            NextToPipe=False
        for i in range(10):
            jumpy-=24
            Mario.goto(curMx,jumpy)
            screen.update()
    if  Mario.ycor()==-228:
        for u in range(16):
            jumpy+=15
            Mario.goto(curMx,jumpy)
            screen.update()
            if checkcollision()==True:
                for i in range(u+1):
                    newYPosition=Mario.ycor()-(15)
                    Mario.goto(curMx, newYPosition)
                    screen.update()
                return
            if checkcolliosion2()==True:
                for i in range(u+1):
                    newYPosition = Mario.ycor() - (15)
                    Mario.goto(curMx, newYPosition)
                    screen.update()
                return
            if checkstandingQ()==True:
                qux = Mario.xcor()
                Mario.goto(qux,questionycoordinate)
                screen.update()
                MarioUpLevels+=1
                return
            if checkstandingH()==True:
                qux = Mario.xcor()
                Mario.goto(qux,questionycoordinate)
                screen.update()
                MarioUpLevels+=1
                return
        if NextToPipe==True:
            NextToPipe=False
        for i in range(10):
            jumpy-=24
            Mario.goto(curMx,jumpy)
            screen.update()
    if abs(Mario.ycor()-Floor2Level)<=0.5:
        for u in range(16):
            jumpy+=15
            Mario.goto(curMx,jumpy)
            screen.update()
            if checkcollision()==True:
                for i in range(u+1):
                    newYPosition=Mario.ycor()-(15)
                    Mario.goto(curMx, newYPosition)
                    screen.update()
                return
            if checkcolliosion2()==True:
                for i in range(u+1):
                    newYPosition = Mario.ycor() - (15)
                    Mario.goto(curMx, newYPosition)
                    screen.update()
                return
        for i in range(10):
            jumpy-=24
            Mario.goto(curMx,jumpy)
            screen.update()
walk_speed=13
def sprint():
    global walk_speed
    walk_speed+=15
def slow():
    global walk_speed
    walk_speed-=10

def right():
    global notStandingGlobal
    Mux=Mario.xcor()
    Muy=Mario.ycor()
    global NextToPipe
    if NextToPipe==False:
        for i in NotMario:
            for j in i:
                j.backward(walk_speed)
    if checkNotStandingQ0()==True and checkNotStandingQ1()==True and checkNotStandingH0()==True and checkNotStandingH1():
        for i in range(10):
            Muy -= 18.45
            Mario.goto(Mux, Muy)
            screen.update()
        return
    if checkNotStandingP()==True:
        for i in range(5):
            Muy-=23.3
            Mario.goto(Mux, Muy)
            screen.update()
def left():
    Mux = Mario.xcor()
    Muy = Mario.ycor()
    global NextToPipe
    if NextToPipe == False:
        for i in NotMario:
            for j in i:
                j.backward(-1*walk_speed)
    if checkNotStandingQ0()==True and checkNotStandingQ1()==True and checkNotStandingH0()==True and checkNotStandingH1():
        for i in range(10):
            Muy -= 18.45
            Mario.goto(Mux, Muy)
            screen.update()
        return
    if checkNotStandingP()==True:
        for i in range(5):
            Muy-=23.3
            Mario.goto(Mux, Muy)
            screen.update()
    screen.update()
screen.onkey(jump,"w")
screen.onkey(jump,"W")
screen.onkey(right,"d")
screen.onkey(right,"D")
screen.onkey(left,"a")
screen.onkey(left,"A")
screen.onkeypress(sprint, "F")
screen.onkeypress(sprint, "f")
screen.onkeyrelease(slow, "F")
screen.onkeyrelease(slow, "f")
screen.listen()
triggerCheck=False
checky=True
t0=time.time()
t2=400
while True:
    Count_Coin.clear()
    Count_Coin.write(coincount,align='left',font=('Emulogic',18,'normal'))
    Point_counter.clear()
    if len(str(points))==1:
        point_string="00000"+str(points)
    elif len(str(points))==2:
        point_string="0000"+str(points)
    elif len(str(points))==3:
        point_string="000"+str(points)
    elif len(str(points))==4:
        point_string="00"+str(points)
    elif len(str(points))==5:
        point_string="0"+str(points)
    Point_counter.write(point_string,align='left',font=('Emulogic',18,'normal'))
    checkcolliosionPipe()
    if t2>0:
        t1=time.time()-t0
        t2=400-t1
        Timer.clear()
        Timer.write(int(t2),align='left',font=('Emulogic',18,'normal'))
    if checky==True:
        if abs(Mario.xcor()-triggerg.xcor())<=50:
            spawn=Goombas[0]
            spawn.goto(Mario.xcor()+150, -341)
            screen.update()
            triggerCheck=True
            checky=False
    if triggerCheck:
        spawn.backward(5.5)
        screen.update()
    for gooma in Goombas:
        if abs(Mario.xcor()-gooma.xcor())<=38 and abs(Mario.ycor()-gooma.ycor())<=60:
            G_stomped(gooma)
            screen.update()
            points+=100
    for i in Goombas:
        if abs(Mario.xcor()-i.xcor())<=57  and abs(Mario.ycor()-i.ycor())<=8:
            M_die()
            screen.update()
            break
    for i in Mushroom:
        i.forward(5)
        Mushx = i.xcor()
        Mushy = i.ycor()
        if checkMNotStandingQ0() == True and checkMNotStandingQ1() == True and checkMNotStandingH0() == True and checkMNotStandingH1():
            for j in range(10):
                Mushy -= 18.45
                i.goto(Mushx, Mushy)
                screen.update()
    for i in Mushroom:
        if abs(Mario.xcor()-i.xcor())<20 and abs(Mario.ycor()-i.ycor())<20:
            points+=1000
            i.write(1000,align='left',font=('Emulogic',10,'normal'))
            i.ht()
    screen.update()






turtle.Screen().exitonclick()
