import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Turtle Board")

turtle_instance = turtle.Turtle()
turtle_instance.color("dark blue")
turtle.speed(0)

color_list = ["red","blue","orange","yellow","purple","brown"]

for i in range(10):
    turtle_instance.color(color_list[i % 6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)


turtle.done()