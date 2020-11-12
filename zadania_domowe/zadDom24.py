from turtle import *
from math import *

def drawSpace():
    penup()
    forward(40)
    left(90)
    forward(200)
    right(90)

def draw1():
    penup()
    forward(50)
    right(90)
    pendown()
    forward(200)
    left(90)
    penup()
    forward(50)

def draw2():
    pendown()
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    penup()

def draw3():
    pendown()
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(180)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    penup()
    left(180)
    forward(100)

def draw7():
    pendown()
    forward(100)
    right(90)
    forward(200)
    penup()

penup()
shape('turtle')
goto(-200, 200)
# speed(2137)
draw2()
drawSpace()
draw1()
drawSpace()
draw3()
drawSpace()
draw7()
drawSpace()
done()

for letter in "abcde":
    print(letter)