import random
from turtle import *

screen = Screen()

t = Turtle()
g = Turtle()
h = Turtle()
b = Turtle()


t.color("red")
g.color("pink")
h.color("orange")
b.color("yellow")

user_bet = screen.textinput("Make your bet", "Which turtle will win? red/pink/orange/yellow")

t.shape("turtle")
g.shape("turtle")
h.shape("turtle")
b.shape("turtle")

t.penup()
b.penup()
g.penup()
h.penup()

t.goto(-200, -150)
b.goto(-200, -50)
g.goto(-200, 50)
h.goto(-200, 150)

t.pendown()
b.pendown()
g.pendown()
h.pendown()

winner = None


for i in range(100):

    t_step = random.randint(0, 20)
    b_step = random.randint(0, 20)
    h_step = random.randint(0, 20)
    g_step = random.randint(0, 20)

    t.fd(t_step)
    b.fd(b_step)
    h.fd(h_step)
    g.fd(g_step)

    if t.xcor() >= 200 and winner is None:
        winner = "red"
    elif b.xcor() >= 200 and winner is None:
        winner = "yellow"
    elif h.xcor() >= 200 and winner is None:
        winner = "orange"
    elif g.xcor() >= 200 and winner is None:
        winner = "pink"

    if winner:
        break

if winner:
    if user_bet and user_bet.lower() == winner:
        textinput("🎉 Congratulations!", f"Your {winner} turtle won!")
    else:
        textinput("Game Over", f"The {winner} turtle won. You bet on {user_bet}.")
else:
    textinput("Race Finished", "No turtle reached the finish line!")

screen.exitonclick()