import turtle

turtle.shape('turtle')
turtle.pencolor('blue')
turtle.pensize(5)

lados=6
mosaico=10
pen=5

for i in range(0,mosaico):
    turtle.right(360/mosaico)
    for i in range(0,lados):
        turtle.forward(100)
        turtle.right(360/lados)
        turtle.pensize(pen-1)
    
turtle.delay(30000)

#el circulo se hace con un for con 360 veces 