from turtle import *
import turtle
pen = turtle.Turtle()
ss = turtle.Screen()
ss.bgcolor('black')
pen.pensize(9)
pen.color('#00adef')


def rect(): # length 340 # breadth 182
    
    alphabets = numinput('Enter in number:', 'How many Alphabets your name contains?', 4, minval= 4, maxval= 15)
    if alphabets == 4:
        upperline = 330
        bottom_line = 170
    elif alphabets == 5:
        upperline = 415
        bottom_line = 400
        pen.goto(30, 0)
    elif alphabets ==6:
        upperline = 510
        bottom_line = 420
        pen.goto(70, 0)
    elif alphabets  == 7:
        upperline = 580
        bottom_line = 420
        pen.goto(120, 0)

    pen.pensize(9)
    pen.forward(170) #bottom starting line of rect
    pen.left(45)
    pen.forward(6)
    pen.left(45)
    pen.forward(170) #right breadth of rect
    pen.left(45)
    pen.forward(6)
    pen.left(45)
    pen.forward(upperline) #upper line of rect 
    pen.left(45)
    pen.forward(6)
    pen.left(45)
    pen.forward(170)  #left breadth of rect
    pen.left(45)
    pen.forward(6)
    pen.left(45)
    pen.forward(bottom_line) #bottom ending line of rect

    pen.backward(bottom_line - 20)
    pen.lt(90)
    pen.penup()
    pen.fd(20)
    pen.pendown()
    
def A():
    pen.fd(130) #beginning line of A
    pen.rt(90)
    pen.fd(60) #top line 
    pen.rt(90)
    pen.fd(65) #half line 
    pen.rt(90)
    pen.fd(60) #middle line 
    pen.backward(60)
    pen.lt(90) 
    pen.fd(65) #down going line
    pen.penup()
    pen.lt(90)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def B():
    pen.fd(130)  #starting long line ofB
    pen.rt(90)
    pen.fd(60) #top line
    pen.rt(45)
    pen.fd(6)
    pen.rt(45)
    pen.fd(53) #right upper line
    pen.rt(45)
    pen.fd(6)
    pen.rt(45)
    pen.fd(60) #middle line
    pen.lt(90)
    pen.fd(6)
    pen.lt(90)
    pen.fd(60) #middle returning line
    pen.rt(45)
    pen.fd(6)
    pen.rt(45)
    pen.fd(53) # right lower line
    pen.rt(45)
    pen.fd(6)
    pen.rt(45)
    pen.fd(59) #bottom line
    pen.penup()
    pen.backward(80)
    pen.rt(90)
    pen.pendown()

def C():
    pen.penup()
    pen.fd(130) #simply going up line of C
    pen.rt(90)
    pen.fd(60) #simply going right 
    pen.lt(180)
    pen.pendown()
    pen.fd(56) # top line coming back
    pen.lt(45)
    pen.fd(6)
    pen.lt(45)
    pen.fd(121) #long line
    pen.lt(45)
    pen.fd(6)
    pen.lt(45)  #bottom line
    pen.fd(56)
    pen.penup()
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def D():
    pen.fd(130) #beginning line of D
    pen.rt(90)
    pen.fd(56) #top line
    pen.rt(45)
    pen.fd(6)
    pen.rt(45)
    pen.fd(121) #right line
    pen.rt(45)
    pen.fd(6)
    pen.rt(45)
    pen.fd(55) #bottom line
    pen.penup()
    pen.backward(75)
    pen.rt(90)
    pen.pendown()


def E():
    pen.fd(130) #long line of E
    pen.rt(90)
    pen.fd(60) #top line
    pen.rt(90)
    pen.penup()
    pen.fd(65) #empty top right line
    pen.rt(90)
    pen.fd(20) #tiny space to middle line
    pen.pendown()
    pen.fd(40) #middle line
    pen.penup()
    pen.backward(60)
    pen.lt(90)
    pen.fd(65) #empty bottom right line
    pen.rt(90)
    pen.pendown()
    pen.fd(60) #bottom line
    pen.penup()
    pen.backward(80)
    pen.rt(90)
    pen.pendown()

def F():
    pen.fd(130) #longest line of F
    pen.rt(90)
    pen.fd(60) #top line
    pen.rt(90)
    pen.penup()
    pen.fd(65) #gap on top right
    pen.rt(90)
    pen.fd(20) #small gap in middle line
    pen.pendown()
    pen.fd(40) #middle line
    pen.penup()
    pen.backward(60)
    pen.lt(90)
    pen.fd(65) #gap on bottom right
    pen.lt(90)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def G():
    pen.penup()
    pen.fd(130) #simply going up line of G
    pen.rt(90)
    pen.fd(60) #simply going right 
    pen.lt(180)
    pen.pendown()
    pen.fd(56) # top line coming back
    pen.lt(45)
    pen.fd(6)
    pen.lt(45)
    pen.fd(121) #long line
    pen.lt(45)
    pen.fd(6)
    pen.lt(45)  #bottom line
    pen.fd(50)
    pen.lt(45)
    pen.fd(6)
    pen.lt(45)
    pen.fd(55) #right upgoing line
    pen.lt(45)
    pen.fd(6)
    pen.lt(45)
    pen.fd(30) #middle line
    pen.penup()
    pen.lt(90)
    pen.fd(63) #bottom empty line
    pen.lt(90)
    pen.fd(50)
    pen.lt(90)
    pen.pendown()

def H():
    pen.fd(130) #beginning line of H
    pen.rt(90)
    pen.penup()
    pen.fd(60) #top gap 
    pen.pendown()
    pen.rt(90)
    pen.fd(65) #half line 
    pen.rt(90)
    pen.fd(60) #middle line 
    pen.backward(60)
    pen.lt(90) 
    pen.fd(65) #down going line
    pen.penup()
    pen.lt(90)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def I():
    pen.penup()
    pen.fd(130) #gap going up
    pen.pendown()
    pen.rt(90)
    pen.fd(60) #upper line of I
    pen.backward(30)
    pen.rt(90)
    pen.fd(130) #middle line
    pen.lt(90)
    pen.fd(30) #lower half line
    pen.backward(60) #lower half line going back
    pen.penup()
    pen.fd(80) #gap between two letters
    pen.lt(90)
    pen.pendown()
    
def J():
    pen.penup()
    pen.fd(130) #gap going up
    pen.rt(90)
    pen.pendown()
    pen.fd(60) #upper line of J
    pen.backward(30) #line coming in between
    pen.rt(90)
    pen.fd(102) #longest middle line
    pen.rt(45)
    pen.fd(40) #curve line
    pen.lt(135)
    pen.penup()
    pen.fd(77)
    pen.lt(90)
    pen.pendown()

def K():
    pen.fd(130) #longest line of K
    pen.backward(65) #come to middle
    pen.rt(45) 
    ksize = 85
    pen.fd(ksize) #upper cross line
    pen.backward(ksize)
    pen.rt(95)
    pen.fd(ksize) #lower cross line
    pen.rt(130)
    pen.penup()
    pen.fd(56)
    pen.backward(80)
    pen.rt(90)
    pen.pendown()

def L():
    pen.fd(130) #long line of L
    pen.backward(130)
    pen.rt(90)
    pen.fd(60) #bottom line
    pen.penup()
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def M():
    
    pen.fd(130) #left big line of M
    pen.rt(150)
    pen.fd(60) #small left cross line 
    pen.lt(120)
    pen.fd(60) #small right cross line
    pen.rt(150)
    pen.fd(130) #big line at right
    pen.penup()
    pen.lt(90)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def N():
    pen.fd(130) #big line of left in N
    pen.rt(160)
    pen.fd(140) #big line in between 
    pen.lt(160)
    pen.fd(130) #big line on right
    pen.backward(130)
    pen.penup()
    pen.rt(90)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def O():
    pen.fd(130) #left line of O
    pen.rt(90)
    pen.fd(60) #upper short line
    pen.rt(90)
    pen.fd(130) #line at right side
    pen.rt(90)
    pen.fd(60) #bottom line
    pen.penup()
    pen.backward(80)
    pen.rt(90)
    pen.pendown()
    
def P():
    pen.fd(130) #long line of P
    pen.rt(90)
    pen.fd(60) #upper line 
    pen.rt(90)
    pen.fd(65) #line at the right
    pen.rt(90)
    pen.fd(60) #line in between
    pen.penup()
    pen.lt(90)
    pen.fd(65)
    pen.lt(90)
    pen.fd(80)
    pen.lt(90)
    pen.pendown()

def Q(): 
    pen.fd(130) #line at left side of Q
    pen.rt(90)
    pen.fd(60) #upper line 
    pen.rt(90)
    pen.fd(130) #line at the right
    pen.rt(90)
    pen.fd(60) #lower line
    pen.penup()
    pen.rt(125)
    pen.fd(46)
    pen.pendown()
    pen.rt(100)
    pen.fd(61) #end line
    pen.lt(90)
    pen.penup()
    pen.fd(12)
    pen.rt(45)
    pen.lt(90)
    pen.pendown()
    
def R():
    pen.fd(130) #long line of P
    pen.rt(90)
    pen.fd(60) #upper line 
    pen.rt(90)
    pen.fd(65) #line at the right
    pen.rt(90)
    pen.fd(60) #line in between
    pen.lt(135)
    pen.fd(94)
    pen.penup()
    pen.lt(45)
    pen.fd(12)
    pen.lt(90)
    pen.pendown()
    
def S():
    pen.penup()
    pen.fd(130) #long empty gap of S 
    pen.rt(90)
    pen.fd(60) #upper empty gap
    pen.pendown()
    pen.backward(60) #upper line
    pen.rt(90)
    pen.fd(65) #left line 
    pen.lt(90)
    pen.fd(60) #middle line
    pen.rt(90)
    pen.fd(65)
    pen.rt(90)
    pen.fd(60)
    pen.penup()
    pen.backward(80)
    pen.rt(90)
    pen.pendown()

def T():
    pen.penup()
    pen.fd(130) #left empty line of T
    pen.pendown()
    pen.rt(90) #upper line
    pen.fd(60)
    pen.backward(30)
    pen.rt(90)
    pen.fd(130) #middle long line
    pen.lt(90)
    pen.penup()
    pen.fd(50)
    pen.lt(90)
    pen.pendown()

def U():
    pen.fd(130) #left long line of U
    pen.penup()
    pen.rt(90)
    pen.fd(60) #upper empty gap 
    pen.rt(90)
    pen.pendown()
    pen.fd(130) #long line on right
    pen.rt(90)
    pen.fd(60) #short lower line
    pen.penup()
    pen.backward(80)
    pen.rt(90)
    pen.pendown()

def V():
    pen.penup()
    pen.fd(130) #left big gap of V
    pen.rt(165)
    pen.pendown()
    pen.fd(135) #small left cross line 
    pen.lt(150)
    pen.fd(135) #small right cross line
    pen.rt(165)
    pen.penup()
    pen.fd(130) #big line at right
    pen.lt(90)
    pen.fd(15)
    pen.lt(90)
    pen.pendown()

def W():
    pen.fd(130) #starting line of W
    pen.backward(130)
    pen.rt(35)
    pen.fd(65) #small left line
    pen.rt(114)
    pen.fd(65) #small right line
    pen.lt(149)
    pen.fd(130) #big right line
    pen.backward(130)
    pen.penup()
    pen.rt(90)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()

def X():
    pen.rt(24)
    pen.fd(140) #cross line of X
    pen.penup()
    pen.lt(114)
    pen.fd(60) #upper gap 
    pen.pendown()
    pen.lt(115)
    pen.fd(140) #cross line
    pen.penup()
    pen.lt(65)
    pen.fd(20)
    pen.lt(90)
    pen.pendown()
    
def Y():
    pen.penup()
    pen.fd(130)
    pen.pendown()
    pen.rt(155)
    pen.fd(65)
    pen.lt(130)
    pen.fd(65)
    pen.backward(65)
    pen.lt(25)
    pen.backward(69)
    pen.rt(90)
    pen.penup()
    pen.fd(45)
    pen.lt(90)
    pen.pendown()

def Z():
    pen.penup()   
    pen.fd(130)
    pen.pendown()
    pen.rt(90)
    pen.fd(60)
    pen.rt(115)
    pen.fd(143)
    pen.lt(115)
    pen.fd(60)
    pen.penup()
    pen.fd(15)
    pen.lt(90)
    pen.pendown()

rect()
#write the alphabets of your name in capital letters
F()
A()
R()
O()
O()
Q()

pen.hideturtle()
done()