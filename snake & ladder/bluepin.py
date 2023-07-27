
                if picknumber() and turn=="red":
                    turn ="blue"
                    if diceroll==1 and b1x==20 and b1y==690:
                        b1x=98
                        b1y=690
                        turn="red"

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
                        turn="red"


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
                        turn="red"

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
                        turn="red"
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
                        turn="red"


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
                        turn="red"

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
                        turn="red"
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
                        turn ="red"

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
                        turn="red"
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
                        turn="red"
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
                        turn="red"

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
                        turn="red"
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
                        turn="red"
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
                        turn="red"
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
                        turn="red"
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
                        
                        turn="red"


                    #final row
                    elif b1y==15 and (b1x==698 or b1x==773) and diceroll!=6:
                        b1x=b1x-(75*diceroll)
                    elif b1y==15 and (b1x==698 or b1x==773) and diceroll==6:
                        b1x=b1x-(75*diceroll)
                        turn="red"
                    elif b1y==15 and b1x==548 and diceroll<5:
                        b1x=b1x-(75*diceroll)
                    elif b1y==15 and b1x==548 and diceroll==5:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==5:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==548 and diceroll==6:
                        b1x=b1x
                    elif b1y==15 and b1x==623 and diceroll!=6:
                        b1x=b1x-(75*diceroll)
                    elif b1y==15 and b1x==505 and diceroll==6:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==6:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==473 and diceroll<6:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==6 and diceroll==4:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==473 and b1x>=98 and diceroll==6:
                        b1x=b1x
                    elif b1y==15 and b1x==398 and b1x>=98 and diceroll>=5:
                        b1x=b1x
                    elif b1y==15 and b1x==398 and b1x>=98 and diceroll<5:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==3:
                            b1x=98
                            b1y=390
                    elif b1y==6 and b1x==323 and b1x>=98 and diceroll>=4:
                        b1x=b1x
                    elif b1y==6 and b1x==323 and b1x>=98 and diceroll<4:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==2:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==248 and b1x>=98 and diceroll>=3:
                        b1x=b1x
                    elif b1y==15 and b1x==248 and b1x>=98 and diceroll<3:
                        b1x=b1x-(75*diceroll)
                        if b1x==173 and b1y==15 and diceroll==1:
                            b1x=98
                            b1y=390
                    elif b1y==15 and b1x==173 and b1x>98 and diceroll>=2:
                        b1x=b1x
