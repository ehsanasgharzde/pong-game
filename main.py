from turtle import Screen
from player import Player
from border import Border
from scoreboard import ScoreBoard
import time
from ball import Ball


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

scoreboard = ScoreBoard()
scoreboard.updatescoreboard()
scoreboard.welcome()

border = Border()

leftplayer = Player('leftplayer')
rightplayer = Player('rightplayer')

ball = Ball()

screen.listen()
screen.onkey(rightplayer.up, 'Up')
screen.onkey(rightplayer.down, 'Down')
screen.onkey(leftplayer.up, 'w')
screen.onkey(leftplayer.down, 's')

gameon = True

while gameon:
    screen.update()
    time.sleep(ball.timeset)

    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()

    # Detect collision with paddles
    if ball.distance(rightplayer) < 40 and ball.xcor() > 320 or ball.distance(leftplayer) < 40 and ball.xcor() < -320:
        ball.xbounce()

    # Detect when right player misses
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.leftpoint()
    
    # Detect when left player misses
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.rightpoint()


screen.exitonclick()