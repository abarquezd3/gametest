from tkinter import *
from tkinter.ttk import*
import turtle 

paddle_speed = 30
ball_spped = 0.09

wm = turtle.Screen()
wm.title("Ping pong")
wm.bgcolor("black")
wm.setup(width=1980, height=1080)
wm.tracer(0)

score_red = 0
score_blue = 0

paddle_red = turtle.Turtle()
paddle_red.speed(0)
paddle_red.shape("square")
paddle_red.color("red")
paddle_red.shapesize(stretch_wid=7, stretch_len=1)
paddle_red.penup()
paddle_red.goto(-650, 0)

paddle_blue = turtle.Turtle()
paddle_blue.speed(0)
paddle_blue.shape("square")
paddle_blue.color("blue")
paddle_blue.shapesize(stretch_wid=7, stretch_len=1)
paddle_blue.penup()
paddle_blue.goto(650, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_spped
ball.dy = ball_spped

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,400)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24, "normal"))

# red movement
def paddle_red_up():
    y = paddle_red.ycor()
    y += paddle_speed
    paddle_red.sety(y)
def paddle_red_down():
    y = paddle_red.ycor()
    y -= paddle_speed
    paddle_red.sety(y)

# blue movement
def paddle_blue_up():
    y = paddle_blue.ycor()
    y += paddle_speed
    paddle_blue.sety(y)

def paddle_blue_down():
    y = paddle_blue.ycor()
    y -= paddle_speed
    paddle_blue.sety(y)

wm.listen()
wm.onkeypress(paddle_red_up, "w")
wm.onkeypress(paddle_red_down, "s")
wm.onkeypress(paddle_blue_up, "Up")
wm.onkeypress(paddle_blue_down, "Down")

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    wm.update()
    
    #wall
    if ball.ycor() > 500:
        ball.sety(500)
        ball.dy *= -1
    if ball.ycor() < -500:
        ball.sety(-500)
        ball.dy *= -1

    if ball.xcor() > 950:
        ball.goto(0,0)
        ball.dx *=-1
        score_red +=1
        pen.clear()
        pen.write("Player Red: {} Player Blue: {}".format(score_red, score_blue), align="center", font=("Courier",24, "normal"))
    if ball.xcor() < -950:
        ball.goto(0,0)
        ball.dx *=-1
        score_blue +=1 
        pen.clear()
        pen.write("Player Red: {} Player Blue: {}".format(score_red, score_blue), align="center", font=("Courier",24, "normal"))

    #collision
    if (ball.xcor() > 630 and ball.xcor() < 650) and (ball.ycor() < paddle_blue.ycor() + 70 and ball.ycor()  > paddle_blue.ycor() - 70): 
        ball.setx(610)
        ball.dx *= -1
    if (ball.xcor() < -630 and ball.xcor() > -650) and (ball.ycor() < paddle_red.ycor() + 70 and ball.ycor()  > paddle_red.ycor() - 70): 
        ball.setx(-610)
        ball.dx *= -1