from turtle import Turtle,Screen
import random
is_race_on=True
scr=Screen()
scr.setup(500,400)
user_turtle=scr.textinput(title="Choose your Turtle",prompt="Choose the color of your turtle : ")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    tammy = Turtle(shape="turtle")
    tammy.color(colors[turtle_index])
    tammy.penup()
    tammy.goto(-230,y_positions[turtle_index])
    all_turtles.append(tammy)

if user_turtle:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on=False
            winner=turtle.pencolor()
            if winner==user_turtle:
                print(f"You won. The {winner} turtle is the winner")
            else:
                print(f"You lost. The {winner} turtle is the winner")

        tspeed=random.randint(0,10)
        turtle.forward(tspeed)
scr.exitonclick()

