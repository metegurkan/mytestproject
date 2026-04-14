import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("gold")
turtle_screen.title("Turtle Board")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
shrinkingSquare(10)

turtle.done()

