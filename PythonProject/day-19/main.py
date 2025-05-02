from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle  will win the race?")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-90, -60, -20, 40, 70, 110]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
            if turtle.xcor() >230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("You have won! The " + winning_color + " turtle is the winner!")
                else:
                    print("You have lost! The " + winning_color + " turtle is the winner!")

            random_distance = random.randint(0, 50)
            turtle.forward(random_distance)



screen.exitonclick()
