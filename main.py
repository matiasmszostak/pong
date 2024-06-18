import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

l_paddle = Paddle(LEFT_PADDLE_POSITION)
r_paddle = Paddle(RIGHT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO: When the ball hits the edge of the paddle, it increase its speed too much

    # Right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
