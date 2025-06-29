import random
import turtle
t=turtle.Turtle()
t.hideturtle()
turtle.bgcolor("black")


t.penup()
t.speed(100)


b = [-1,-2,-3,1,2,3]
c = [1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200] #b,c = wyliczanie koordynatow punktu
x = ""
y = "" #x,y = wyliczone koordynaty
k = ["red","lime","purple","orange","lightblue","yellow","#FF0043","#FFFFFF","#F8FF00","#00A0FF"]






for i in range(1000):
    t.penup()
    random.shuffle(k)
    random.shuffle(b)
    random.shuffle(c)
    x = b[1] * c[1]
    random.shuffle(b)
    random.shuffle(c)
    y = b[1] * c[1]


    t.color(k[1])
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.pendown()
    
    t.forward(20)
    t.right(135)

    random.shuffle(k)
    t.color(k[1])

    t.forward(25)
    t.right(150)

    random.shuffle(k)
    t.color(k[1])

    t.forward(30)
    t.right(150)

    random.shuffle(k)
    t.color(k[1])

    t.forward(30)
    t.right(150)

    random.shuffle(k)
    t.color(k[1])
    
    t.forward(25)
    t.right(135)
    t.end_fill()


    


turtle.exitonclick()