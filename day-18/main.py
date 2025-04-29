import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

#direction = [0,90,180,270]

# for _ in range(1000):
#     tim.speed("fastest")
#     tim.color(random_color())
#     tim.pensize(5)
#     tim.forward(10)
#     tim.setheading(random.choice(direction))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.speed("fastest")

draw_spirograph(5)




screen = t.Screen()
screen.exitonclick()