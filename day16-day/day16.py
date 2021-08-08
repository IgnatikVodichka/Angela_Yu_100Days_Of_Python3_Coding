from turtle import Turtle, Screen  # these are the Classes included in pre-installed "turtle" module of Turtle Graphics.


tacito = Turtle()
tacito.shape("turtle")  # giving our turtle a shape of an actual turtle.
tacito.color("black", "DarkSeaGreen4")
tacito.forward(100)

my_screen = Screen()
my_screen.exitonclick()  # screen will quit only if click detected on it.
