import turtle
import random

lines=random.randint(5,10)

for x in range(0,lines):
    largo=random.randint(25,100)
    rotacion=random.randint(1,360)
    turtle.forward(largo)
    turtle.right(rotacion)
    
    
    
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.circle(20)

turtle.exitonclick