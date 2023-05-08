from turtle import Screen, Turtle

pantalla=Screen()
pantalla.setup(425,225) #Borde externo
pantalla.screensize(400,200) #Borde interno
pantalla.setworldcoordinates(-50,-150,350,250) #Esquina inferior izquierda y superior derecha

tortuga=Turtle()
tortuga.forward(100)

tortuga.penup()
tortuga.right(90)
tortuga.forward(10)
tortuga.right(90)

tortuga.pendown()
tortuga.forward(100)

pantalla.exitonclick()