import pygame
import random
import time



pygame.init()

screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("Snakes & Ladders")

#background

bckimg=pygame.image.load("snake and ladders.jpg")
roll_dice=pygame.image.load("dice roll.jpg")

bx=95
by=5

rdx=850
rdy=10

#players
r1=pygame.image.load("red pin(S&L).jpg")
b1=pygame.image.load("blue pin(S&L).jpg")

rx=20
ry=690

b1x=20
b1y=600

button=pygame.Rect(rdx,rdy,260,260)

font1=pygame.font.SysFont("comicsansms" , 20)

#clock=pygame.time.Clock()



def bck():
    screen.blit(bckimg,(bx,by))
    screen.blit(roll_dice,(rdx,rdy))

def rplayer(x,y):
    screen.blit(r1,(x,y))

def bplayer(x,y):
    screen.blit(b1,(x,y))

def picknumber():
    diceroll=random.randint(1,6)
    if diceroll==1:
        dice=pygame.image.load("dice1.jpg")
    elif diceroll==2:
        dice=pygame.image.load("dice2.jpg")
    elif diceroll==3:
        dice=pygame.image.load("dice3.jpg")
    elif diceroll==4:
        dice=pygame.image.load("dice4.jpg")
    elif diceroll==5:
        dice=pygame.image.load("dice5.jpg")
    elif diceroll==6:
        dice=pygame.image.load("dice6.jpg")

    return(dice,diceroll)


def rollr():
    msg1=font1.render("RED'S TURN" , True , (255,255,255))
    screen.blit(msg1,[5,755])

def rollb():
    msg2=font1.render("BLUE's TURN" , True , (255,255,255))
    screen.blit(msg2,[5,560])
    

#game loop

running = True

turn="red"
while running:
    screen.fill((0,255,195))
    bck()

    if turn =="red":
        rollr()
    else:
        rollb()



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                picknumber()
                dice,diceroll=picknumber()
                screen.blit(dice,(900,300))
                print(diceroll)

                #for player 1

                if picknumber() and turn=="red":
                    turn ="blue"
                    if diceroll==1 and rx==20 and ry==690:
                        rx=98
                        ry=690
                        turn="red"

                        #row1

                    elif rx in range(98,398) and diceroll!=6 and (ry==690 or ry==540 or ry==390 or ry==240 or ry==90):

                        rx=rx+(75*diceroll)

                        if rx==323 and ry==690:
                            rx=398
                            ry=540
                        elif rx==548 and ry==540:
                            rx=398
                            ry=690
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248  and ry==390:
                            rx=248
                            ry=615
                        elif rx==773 and ry==390:
                            rx=698
                            ry=240
                        elif rx==473 and ry==240:
                            rx=398
                            ry=390
                        elif rx==698 and ry==90:
                            rx=623
                            ry=315
                    

                    elif rx in range(98,398) and diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*diceroll)

                        if rx==323 and ry==690:
                            rx=398
                            ry=540
                        elif rx==548 and ry==540:
                            rx=398
                            ry=690
                        elif rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry== 390:
                            rx=248
                            ry=615
                        elif rx==773 and ry==390:
                            rx=698
                            ry=240
                        elif rx==473 and ry==240:
                            rx=398
                            ry=390
                        elif rx==698 and ry==90:
                            rx=623
                            ry=315
                        turn="red"


                    elif rx==398 and diceroll!=6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*diceroll)
                        if rx==548 and ry==540:
                            rx=398
                            ry=690
                        elif rx==773 and ry==390:
                            rx=698
                            ry=240
                        elif rx==473 and ry==240:
                            rx=398
                            ry=390
                        elif rx==698 and ry==90 and diceroll==4:
                            rx=623
                            ry=315


                    elif rx==398 and diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*5)-(75*(diceroll-6))
                        ry=ry-75
                        turn="red"

                    elif rx==473 and diceroll<=4 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*diceroll)
                        if rx==548 and ry==540:
                            rx=398
                            ry=690
                        elif rx==773 and ry==390:
                            rx=698
                            ry=240
                        elif rx==698 and ry==90 and diceroll==3:
                            rx=623
                            ry=315




                    elif rx==473 and diceroll>4 and diceroll!=6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*4)-(75*(diceroll-5))
                        ry=ry-75
                    elif rx==473 and diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*4)-(75*(diceroll-5))
                        ry=ry-75
                        turn="red"
                    elif rx==548 and diceroll<=3 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*diceroll)

                        if rx==773 and ry==390:
                            rx=698
                            ry=240
                        elif rx==698 and ry==90 and diceroll==2:
                            rx=623
                            ry=240
                    elif rx==548 and diceroll>3 and diceroll!=6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*3)-(75*(diceroll-4))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390

                    elif rx==548 and diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*3)-(75*(diceroll-4))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390
                        turn="red"


                    elif rx==623 and diceroll<=2 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*diceroll)
                        if rx==773 and ry==390:
                            rx=698
                            ry=240
                        elif rx==698 and ry==90:
                            rx=623
                            ry=315

                    elif rx==623 and diceroll>2 and diceroll!=6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*2)-(75*(diceroll-3))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==548 and ry==165:
                            rx=698
                            ry=15

                    elif rx==623 and  diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*2)-(75*(diceroll-3))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==548 and ry==165:
                            rx=698
                            ry=15
                        turn="red"

                    elif rx==698 and diceroll==1 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*diceroll)
                        if rx==773 and ry==390:
                            rx=698
                            ry=240
                    elif rx==698 and diceroll>1 and diceroll!=6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*1)-(75*(diceroll-2))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==548 and ry==165:
                            rx=698 
                            ry=15
                    elif rx==698 and diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx+(75*1)-(75*(diceroll-2))
                        ry=ry-75

                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698 
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==548 and ry==165:
                            rx=698
                            ry=15
                        turn="red"
                    elif rx>=773 and diceroll!=6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx-(75*(diceroll-1))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698 
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==398 and ry==165:
                            rx=248
                            ry=315
                
                    elif rx==773 and diceroll==6 and (ry==690  or ry==540 or ry==390 or ry==240 or ry==90):
                        rx=rx-(49*(diceroll-1))
                        ry=ry-75
                        if rx==623 and ry==615:
                            rx=473 
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==398 and ry==165:
                            rx=248
                            ry=315
                        turn ="red"

                        #row2
                    elif rx>398 and rx<=773 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15) and diceroll!=6:
                        rx=rx-(75*diceroll)
                        if rx==623 and ry==615:
                            rx=473
                            ry=390
                        elif rx==623 and ry==465:
                            rx=698
                            ry=390
                        elif rx==548 and ry==315:
                            rx=773
                            ry=465
                        elif rx==548 and ry==165:
                            rx=698
                            ry=15
                        elif rx==98 and ry==465:
                            rx=248
                            ry=690
                        elif rx==398 and ry==165:
                            rx=248 
                            ry=315

                    elif rx>398 and rx<=773 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) and diceroll==6:
                        rx=rx-(75*diceroll)
                        ry=ry-75
                        turn="red"
                    elif rx>473 and rx<=773 and diceroll!=6 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) :
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15:
                            rx=98 
                            ry=390
                        elif rx==98 and ry==465:
                            rx=248
                            ry=690
                        elif rx==173 and ry==15:
                            rx=98
                            ry=390
                    elif rx>473 and rx<=773 and diceroll==6 and  (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) :
                        rx=rx-(75*diceroll) 
                        if rx==173 and ry==15:
                            rx=98
                            ry=390
                        elif rx==98 and ry==465:
                            rx=248
                            ry=690
                        elif rx==173 and ry==15:
                            rx=98
                            ry=390
                        turn="red"
                    elif rx==473 and diceroll!=6 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) :
                        rx=rx-(75*diceroll)
                        if rx==398 and ry==165:
                            rx=248
                            ry=315
                        elif rx==173 and ry==15:
                            rx=98
                            ry=390
                    elif rx==473  and diceroll==6 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) :
                        rx=rx-(75*5)
                        ry=ry-75
                        if rx==98 and ry==465:
                            rx=248
                            ry=690
                        turn="red"

                    elif rx==398  and diceroll<5 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) :
                        rx=rx-(75*diceroll)
                        if rx==98 and ry==465:
                            rx=248
                            ry=690
                        
                    elif rx==398  and diceroll==5 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15):
                        rx=rx-(75*4)+(75*(diceroll-5))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90

                        
                    elif rx==398  and diceroll==6 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15) :
                        rx=rx-(75*4)+(75*(diceroll-5))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        turn="red"
                    elif rx==323 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15) and diceroll<4:
                        rx=rx-(75*diceroll)
                        if rx==98 and ry==465:
                            rx=248
                            ry=690
                        
                    elif rx==323 and (ry==615  or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll>=4 and diceroll!=6:
                        rx=rx-(75*3)+(75*(diceroll-4))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615

                    elif rx==323 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll==6:
                        rx=rx-(75*3)+(75*(diceroll-4))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==260 and ry==390:
                            rx=248
                            ry=615
                        turn="red"
                    elif rx==248 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll<3:
                        rx=rx-(75*diceroll)
                        if rx==98 and ry==465:
                            rx=248
                            ry=690
                    elif rx==248 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll>=3 and diceroll!=6:
                        rx=rx-(75*2)+(75*(diceroll-3))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615

                    elif rx==248 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)   and diceroll==6:
                        rx=rx-(75*2)+(75*(diceroll-3))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615
                        turn="red"
                    elif rx==173 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll<2:
                        rx=rx-(75*diceroll)
                        if rx==98 and ry==465:
                            rx=248
                            ry=690
                    elif rx==173 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll>=2 and diceroll!=6:
                        rx=rx-(75*1)+(75*(diceroll-2))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248 
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615
                        
                    elif rx==173 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll==6:
                        rx=rx-(75*1)+(75*(diceroll-2))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615
                        turn="red"
                    elif rx==98 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll!=6:
                        rx=rx+(75*(diceroll-1))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615
                        elif rx==473 and ry==240:
                            rx=398
                            ry=390
                    elif rx==98 and (ry==615 or ry==465 or ry==315 or ry==165 or ry==15)  and diceroll==6:
                        rx=rx+(75*(diceroll-1))
                        ry=ry-75
                        if rx==173 and ry==390:
                            rx=248
                            ry=240
                        elif rx==173 and ry==240:
                            rx=98
                            ry=90
                        elif rx==248 and ry==390:
                            rx=248
                            ry=615
                        elif rx==473 and ry==240:
                            rx=398
                            ry=390
                        
                        turn="red"


                    #final row
                    elif ry==15 and (rx==698 or rx==773) and diceroll!=6:
                        rx=rx-(75*diceroll)
                    elif ry==15 and (rx==698 or rx==773) and diceroll==6:
                        rx=rx-(75*diceroll)
                        turn="red"
                    elif ry==15 and rx==548 and diceroll<5:
                        rx=rx-(75*diceroll)
                    elif ry==15 and rx==548 and diceroll==5:
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15 and diceroll==5:
                            rx=98
                            ry=390
                    elif ry==15 and rx==548 and diceroll==6:
                        rx=rx
                    elif ry==15 and rx==623 and diceroll!=6:
                        rx=rx-(75*diceroll)
                    elif ry==15 and rx==623 and diceroll==6:
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15 and diceroll==6:
                            rx=98
                            ry=390
                    elif ry==15 and rx==473 and diceroll<6:
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15 and diceroll==4:
                            rx=98
                            ry=390
                    elif ry==15 and rx==473 and rx>=98 and diceroll==6:
                        rx=rx
                    elif ry==15 and rx==398 and rx>=98 and diceroll>=5:
                        rx=rx
                    elif ry==15 and rx==398 and rx>=98 and diceroll<5:
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15 and diceroll==3:
                            rx=98
                            ry=390
                    elif ry==15 and rx==323 and rx>=98 and diceroll>=4:
                        rx=rx
                    elif ry==15 and rx==323 and rx>=98 and diceroll<4:
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15 and diceroll==2:
                            rx=98
                            ry=390
                    elif ry==15 and rx==248 and rx>=98 and diceroll>=3:
                        rx=rx
                    elif ry==15 and rx==248 and rx>=98 and diceroll<3:
                        rx=rx-(75*diceroll)
                        if rx==173 and ry==15 and diceroll==1:
                            rx=98
                            ry=390
                    elif ry==15 and rx==173 and rx>98 and diceroll>=2:
                        rx=rx






                    


                #for player 2

                elif picknumber() and turn=="blue":
                    turn ="red"
                    if diceroll==1 and b1x==20 and b1y==600:
                        b1x=98
                        b1y=690
                        turn="blue"

                        #row1

                    elif b1x in range(98,398) and diceroll!=6 and (b1y==690 or b1y==540 or b1y==390 or b1y==240 or b1y==90):

                        b1x=b1x+(75*diceroll)

                        if b1x==323 and b1y==690:
                            b1x=398
                            b1y=540
                        elif b1x==548 and b1y==540:
                            b1x=398
                            b1y=690
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248  and b1y==390:
                            b1x=248
                            b1y=615
                        elif b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                        elif b1x==473 and b1y==240:
                            b1x=398
                            b1y=390
                        elif b1x==698 and b1y==90:
                            b1x=623
                            b1y=315
                    

                    elif b1x in range(98,398) and diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*diceroll)

                        if b1x==323 and b1y==690:
                            b1x=398
                            b1y=540
                        elif b1x==548 and b1y==540:
                            b1x=398
                            b1y=690
                        elif b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y== 390:
                            b1x=248
                            b1y=615
                        elif b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                        elif b1x==473 and b1y==240:
                            b1x=398
                            b1y=390
                        elif b1x==698 and b1y==90:
                            b1x=623
                            b1y=315
                        turn="blue"


                    elif b1x==398 and diceroll!=6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*diceroll)
                        if b1x==548 and b1y==540:
                            b1x=398
                            b1y=690
                        elif b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                        elif b1x==473 and b1y==240:
                            b1x=398
                            b1y=390
                        elif b1x==698 and b1y==90 and diceroll==4:
                            b1x=623
                            b1y=315


                    elif b1x==398 and diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*5)-(75*(diceroll-6))
                        b1y=b1y-75
                        turn="blue"

                    elif b1x==473 and diceroll<=4 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*diceroll)
                        if b1x==548 and b1y==540:
                            b1x=398
                            b1y=690
                        elif b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                        elif b1x==698 and b1y==90 and diceroll==3:
                            b1x=623
                            b1y=315




                    elif b1x==473 and diceroll>4 and diceroll!=6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*4)-(75*(diceroll-5))
                        b1y=b1y-75
                    elif b1x==473 and diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*4)-(75*(diceroll-5))
                        b1y=b1y-75
                        turn="blue"
                    elif b1x==548 and diceroll<=3 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*diceroll)

                        if b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                        elif b1x==698 and b1y==90 and diceroll==2:
                            b1x=623
                            b1y=240
                    elif b1x==548 and diceroll>3 and diceroll!=6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*3)-(75*(diceroll-4))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390

                    elif b1x==548 and diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*3)-(75*(diceroll-4))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390
                        turn="blue"


                    elif b1x==623 and diceroll<=2 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*diceroll)
                        if b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                        elif b1x==698 and b1y==90:
                            b1x=623
                            b1y=315

                    elif b1x==623 and diceroll>2 and diceroll!=6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*2)-(75*(diceroll-3))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==548 and b1y==165:
                            b1x=698
                            b1y=15

                    elif b1x==623 and  diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*2)-(75*(diceroll-3))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==548 and b1y==165:
                            b1x=698
                            b1y=15
                        turn="blue"

                    elif b1x==698 and diceroll==1 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*diceroll)
                        if b1x==773 and b1y==390:
                            b1x=698
                            b1y=240
                    elif b1x==698 and diceroll>1 and diceroll!=6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*1)-(75*(diceroll-2))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==548 and b1y==165:
                            b1x=698 
                            b1y=15
                    elif b1x==698 and diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x+(75*1)-(75*(diceroll-2))
                        b1y=b1y-75

                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698 
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==548 and b1y==165:
                            b1x=698
                            b1y=15
                        turn="blue"
                    elif b1x>=773 and diceroll!=6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x-(75*(diceroll-1))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698 
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==398 and b1y==165:
                            b1x=248
                            b1y=315
                
                    elif b1x==773 and diceroll==6 and (b1y==690  or b1y==540 or b1y==390 or b1y==240 or b1y==90):
                        b1x=b1x-(49*(diceroll-1))
                        b1y=b1y-75
                        if b1x==623 and b1y==615:
                            b1x=473 
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==398 and b1y==165:
                            b1x=248
                            b1y=315
                        turn ="blue"

                        #row2
                    elif b1x>398 and b1x<=773 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15) and diceroll!=6:
                        b1x=b1x-(75*diceroll)
                        if b1x==623 and b1y==615:
                            b1x=473
                            b1y=390
                        elif b1x==623 and b1y==465:
                            b1x=698
                            b1y=390
                        elif b1x==548 and b1y==315:
                            b1x=773
                            b1y=465
                        elif b1x==548 and b1y==165:
                            b1x=698
                            b1y=15
                        elif b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                        elif b1x==398 and b1y==165:
                            b1x=248 
                            b1y=315

                    elif b1x>398 and b1x<=773 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) and diceroll==6:
                        b1x=b1x-(75*diceroll)
                        b1y=b1y-75
                        turn="blue"
                    elif b1x>473 and b1x<=773 and diceroll!=6 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) :
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15:
                            b1x=98 
                            b1y=390
                        elif b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                        elif b1x==173 and b1y==15:
                            b1x=98
                            b1y=390
                    elif b1x>473 and b1x<=773 and diceroll==6 and  (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) :
                        b1x=b1x-(75*diceroll) 
                        if b1x==173 and b1y==15:
                            b1x=98
                            b1y=390
                        elif b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                        elif b1x==173 and b1y==15:
                            b1x=98
                            b1y=390
                        turn="blue"
                    elif b1x==473 and diceroll!=6 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) :
                        b1x=b1x-(75*diceroll)
                        if b1x==398 and b1y==165:
                            b1x=248
                            b1y=315
                        elif b1x==173 and b1y==15:
                            b1x=98
                            b1y=390
                    elif b1x==473  and diceroll==6 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) :
                        b1x=b1x-(75*5)
                        b1y=b1y-75
                        if b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                        turn="blue"

                    elif b1x==398  and diceroll<5 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) :
                        b1x=b1x-(75*diceroll)
                        if b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                        
                    elif b1x==398  and diceroll==5 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15):
                        b1x=b1x-(75*4)+(75*(diceroll-5))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90

                        
                    elif b1x==398  and diceroll==6 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15) :
                        b1x=b1x-(75*4)+(75*(diceroll-5))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        turn="blue"
                    elif b1x==323 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15) and diceroll<4:
                        b1x=b1x-(75*diceroll)
                        if b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                        
                    elif b1x==323 and (b1y==615  or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll>=4 and diceroll!=6:
                        b1x=b1x-(75*3)+(75*(diceroll-4))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615

                    elif b1x==323 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll==6:
                        b1x=b1x-(75*3)+(75*(diceroll-4))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==260 and b1y==390:
                            b1x=248
                            b1y=615
                        turn="blue"
                    elif b1x==248 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll<3:
                        b1x=b1x-(75*diceroll)
                        if b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                    elif b1x==248 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll>=3 and diceroll!=6:
                        b1x=b1x-(75*2)+(75*(diceroll-3))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615

                    elif b1x==248 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)   and diceroll==6:
                        b1x=b1x-(75*2)+(75*(diceroll-3))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615
                        turn="blue"
                    elif b1x==173 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll<2:
                        b1x=b1x-(75*diceroll)
                        if b1x==98 and b1y==465:
                            b1x=248
                            b1y=690
                    elif b1x==173 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll>=2 and diceroll!=6:
                        b1x=b1x-(75*1)+(75*(diceroll-2))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248 
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615
                        
                    elif b1x==173 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll==6:
                        b1x=b1x-(75*1)+(75*(diceroll-2))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615
                        turn="blue"
                    elif b1x==98 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll!=6:
                        b1x=b1x+(75*(diceroll-1))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615
                        elif b1x==473 and b1y==240:
                            b1x=398
                            b1y=390
                    elif b1x==98 and (b1y==615 or b1y==465 or b1y==315 or b1y==165 or b1y==15)  and diceroll==6:
                        b1x=b1x+(75*(diceroll-1))
                        b1y=b1y-75
                        if b1x==173 and b1y==390:
                            b1x=248
                            b1y=240
                        elif b1x==173 and b1y==240:
                            b1x=98
                            b1y=90
                        elif b1x==248 and b1y==390:
                            b1x=248
                            b1y=615
                        elif b1x==473 and b1y==240:
                            b1x=398
                            b1y=390
                        
                        turn="blue"


                    #final row
                    elif b1y==15 and (b1x==698 or b1x==773) and diceroll!=6:
                        b1x=b1x-(75*diceroll)
                    elif b1y==15 and (b1x==698 or b1x==773) and diceroll==6:
                        b1x=b1x-(75*diceroll)
                        turn="blue"
                    elif b1y==15 and b1x==548 and diceroll<5:
                        b1x=b1x-(75*diceroll)
                    elif b1y==15 and b1x==548 and diceroll==5:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==5:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==548 and diceroll==6:
                        b1x=b1x
                        b1y=b1y
                    elif b1y==15 and b1x==623 and diceroll!=6:
                        b1x=b1x-(75*diceroll)
                    elif b1y==15 and b1x==623 and diceroll==6:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==6:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==473 and diceroll<=4:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==4:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==473 and b1x>=98 and diceroll==6:
                        b1x=b1x
                        b1y=b1y
                    elif b1y==15 and b1x==398 and b1x>=98 and diceroll>=5:
                        b1x=b1x
                        b1y=b1y
                    elif b1y==15 and b1x==398 and b1x>=98 and diceroll<=3:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==3:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==323 and b1x>=98 and diceroll>=4:
                        b1x=b1x
                        b1y=b1y
                    elif b1y==15 and b1x==323 and b1x>=98 and diceroll<=2:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==2:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==248 and b1x>=98 and diceroll>=3:
                        b1x=b1x
                        b1y=b1y
                    elif b1y==15 and b1x==248 and b1x>=98 and diceroll<=1:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==1:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==173 and b1x>98 and diceroll>=2:
                        b1y=390
                        b1x=98
                        

                    
    rplayer(rx,ry)
    bplayer(b1x,b1y)
    pygame.display.update()

    if rx==98 and ry==15:
        screen.fill((50,153,213))
        value = score_font.render("Red won" , True , (255 , 255 , 102))

        screen.blit(value , [250 , 200])

        running = False

    if b1x==98 and b1y==15:
        screen.fill((50,153,213))
        value = score_font.render(" Blue won" , True , (255 , 255 , 102))

        screen.blit(value , [250 , 200])

        running = False






    time.sleep(1.3)


clock.tick(40)
pygame.quit()
quit()

