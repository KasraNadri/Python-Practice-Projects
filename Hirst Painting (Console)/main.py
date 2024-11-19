import colorgram as clg
import turtle as turtle_module
import random

picked_colors = []
colors = clg.extract('PythonProjects\Hirst Painting (Console)\image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r, g, b)
    picked_colors.append(new_colors)
turtle_module.reset()

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100



for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(picked_colors))
    tim.forward(20)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.forward(0)





screen = turtle_module.Screen()
screen.exitonclick()




