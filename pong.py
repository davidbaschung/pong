from tkinter import *
import time
from math import *
import random

def fescape(event) : fen1.destroy()

def p1up_event(event) : # ---------- mouvements des joueurs
    global move_p1
    if move_p1 == 'up' : move_p1 = 'stop'
    elif move_p1 == 'stop':
        move_p1 = 'up'
        p1up()
    elif move_p1 == 'down' :
        move_p1 = 'stop'
        time.sleep(.01)
        move_p1 = 'up'
        p1up()
def p1up() :
    global x1,y1,player1,move_p1
    if y1 > 0 and move_p1 == 'up':
        y1 -= 5
        can.delete(player1)
        player1 = can.create_polygon((x1,y1),(x1+10,y1),(x1+20,y1+30),(x1+20,y1+70),(x1+10,y1+100),(x1,y1+100),fill="blue")
        fen1.after(10,p1up)
    if y1 <= 0 : move_p1 = 'stop'
def p1down_event(event) :
    global move_p1
    if move_p1 == 'down' : move_p1 = 'stop'
    elif move_p1 == 'stop':
        move_p1 = 'down'
        p1down()
    elif move_p1 == 'up' :
        move_p1 = 'stop'
        time.sleep(.01)
        move_p1 = 'down'
        p1down()
def p1down() :
    global x1,y1,player1,move_p1
    if y1 < 500 and move_p1 == 'down' :
        y1 += 5
        can.delete(player1)
        player1 = can.create_polygon((x1,y1),(x1+10,y1),(x1+20,y1+30),(x1+20,y1+70),(x1+10,y1+100),(x1,y1+100),fill="blue")
        fen1.after(10,p1down)
    if y1 <= 0 : move_p1 = 'stop'

def p2up_event(event) :
    global move_p2
    if move_p2 == 'up' : move_p2 = 'stop'
    elif move_p2 == 'stop':
        move_p2 = 'up'
        p2up()
    elif move_p2 == 'down' :
        move_p2 = 'stop'
        time.sleep(.01)
        move_p2 = 'up'
        p2up()
def p2up() :
    global x2,y2,player2,move_p2
    if y2 > 0 and move_p2 == 'up':
        y2 -= 5
        can.delete(player2)
        player2 = can.create_polygon((x2+20,y2),(x2+10,y2),(x2,y2+30),(x2,y2+70),(x2+10,y2+100),(x2+20,y2+100),fill="red")
        fen1.after(10,p2up)
    if y2 <= 0 : move_p2 = 'stop'
def p2down_event(event) :
    global move_p2
    if move_p2 == 'down' : move_p2 = 'stop'
    elif move_p2 == 'stop':
        move_p2 = 'down'
        p2down()
    elif move_p2 == 'up' :
        move_p2 = 'stop'
        time.sleep(.01)
        move_p2 = 'down'
        p2down()
def p2down() :
    global x2,y2,player2,move_p2
    if y2 < 500 and move_p2 == 'down' :
        y2 += 5
        can.delete(player2)
        player2 = can.create_polygon((x2+20,y2),(x2+10,y2),(x2,y2+30),(x2,y2+70),(x2+10,y2+100),(x2+20,y2+100),fill="red")
        fen1.after(10,p2down)
    if y2 <= 0 : move_p2 = 'stop'

def go_event(event) : # ------------- lancement balle
    global breakgo2,nb_func,xb,yb,alpha,ballspeed, player1,y1,player2,y2
    if breakgo2 == True : fen1.after(10,go)
    breakgo2 = False
    xb,yb = 400,300
    y1,y2 = 250,250
    can.delete(player1,player2)
    player1,player2 = can.create_polygon((x1,y1),(x1+10,y1),(x1+20,y1+30),(x1+20,y1+70),(x1+10,y1+100),(x1,y1+100),fill="blue"),can.create_polygon((x2+20,y2),(x2+10,y2),(x2,y2+30),(x2,y2+70),(x2+10,y2+100),(x2+20,y2+100),fill="red")
    alpha = random.randint(0,1)*3.14159
    
def go() :
    global xb,yb,ball,breakgo2,nb_func,ballspeed,alpha ,x1,y1,score1,x2,y2,score2, winrect,wintext,can
    xb+=ballspeed*cos(alpha)
    yb+=ballspeed*sin(alpha)
    can.delete(ball)
    ball = can.create_oval(xb-20,yb-20,xb+20,yb+20,fill="white",width=2)
    
    if xb-20 <= x1+20 : # ----- raquette 1
        if yb>=y1 and yb<y1+30 and (xb-20)-x1-10 <= (yb-y1)/3 : # plan à 108.43 degrés
            alpha = -alpha +2.8199
            xb+=1
        if yb>=y1+30 and yb<=y1+70 : # plan centre
            alpha = -alpha +3.1415
            xb+=1
        if yb>y1+70 and yb<=y1+100 and (xb-20)-x1-10 <= 10-(yb-(y1+70))/3: # plan à 71.57 degrés
            alpha = -alpha +3.4632
            xb+=1
    if xb+20 >= x2 : # ----- raquette 2
        if yb>=y2 and yb<y2+30 and (xb+20)-x2+0 >= 10-(yb-y2)/3 : # plan à 71.57 degrés
            alpha = -alpha +3.4632
            xb-=1
        if yb>=y2+30 and yb<=y2+70 : # plan centre
            alpha = -alpha +3.1415
            xb-=1
        if yb>y2+70 and yb<=y2+100 and (xb+20)-x2+0 >= (yb-(y2+70))/3 : # plan à 108.43 degrés
            alpha = -alpha +2.8199
            xb-=1
    #### angle : 18.43 degrés
    if yb <= 0 or yb >= 600 : alpha = -alpha # bords supérieur et inférieur du Canvas

    if xb<10 :
        breakgo2=True
        score2 += 1
        score_label2.config(text=f_score2(score2))
    if xb>791 :
        breakgo2=True
        score1 += 1
        score_label1.config(text=f_score1(score1))
    if breakgo2 != True :
        fen1.after(10, go)

    if score1 == 10 :
        winrect = can.create_rectangle(5,250,800,350,fill='yellow',outline='dark orange',width=5)
        wintext = can.create_text(400,300,text='!LE JOUEUR BLEU A GAGNE!',font=('Brutal Tooth',50,'bold'),fill='dark orange')#,bg='yellow')
        #win.pack(padx=0,pady=280)
    if score2 == 10 :
        winrect = can.create_rectangle(5,250,800,350,fill='yellow',outline='dark orange',width=5)
        wintext = can.create_text(400,300,text='!LE JOUEUR ROUGE A GAGNE!',font=('Brutal Tooth',50,'bold'),fill='dark orange')#,bg='yellow')
        #win.pack(padx=0,pady=280)
def breaking_event(event) :
    global breakgo2
    breakgo2 = True

def f_score1(score) :
    if score<10 : return '0'+str(score)
    else : return str(score)
def f_score2(score) :
    if score<10 : return '0'+str(score)
    else : return str(score)
    
    
#---------------------------------------------------------------------------
x1,y1,move_p1, score1 = 0,250,'stop', 0 #joueur 1
x2,y2,move_p2, score2 = 781,250,'stop', 0 #joueur 2
xb,yb,ballspeed, alpha = 400,300,10, 0 #balle
breakgo2 = True

fen1 = Tk()
#fen1.overrideredirect(True)
fen1.geometry("%dx%d%+d%+d" % (824,720,200,0))
fen1.config(bg="dark red")
Label(fen1,text="Jeu de raquettes",font=("Brutal Tooth",30,"normal"),fg="#%02x%02x%02x"%(60,0,0),bg="orange").grid(row=0,column=0)

can = Canvas(fen1,width=800,height=600)
can.grid(row=1,column=0,padx=10,pady=10)
player1 = can.create_polygon((x1,y1),(x1+10,y1),(x1+20,y1+30),(x1+20,y1+70),(x1+10,y1+100),(x1,y1+100),fill="blue")
player2 = can.create_polygon((x2+20,y2),(x2+10,y2),(x2,y2+30),(x2,y2+70),(x2+10,y2+100),(x2+20,y2+100),fill="red")
ball = can.create_oval(xb-20,yb-20,xb+20,yb+20,fill="white",width=2)

score_frame = Frame(width=150,height=40,bg='dark red')
score_frame.grid(column=0,row=2)
score_label1 = Label(score_frame,text=f_score1(score1),font=('DS-Digital',20))
score_label1.pack(padx=25,side=LEFT)
#Label(score_frame,text='          ').pack(side=CENTER)
score_label2 = Label(score_frame,text=f_score2(score2),font=('DS-Digital',20))
score_label2.pack(padx=25,side=RIGHT)
winrect,wintext = False,False

fen1.bind("<a>",p1up_event)
fen1.bind("<y>",p1down_event)
fen1.bind("<Up>",p2up_event)
fen1.bind("<Down>",p2down_event)
fen1.bind("<Escape>",fescape)
fen1.bind("<space>", go_event)
fen1.bind("<f>",breaking_event)
mainloop()
