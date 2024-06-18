from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(35)
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.85

    def reset(self):
        self.setposition(0, 0)
        self.x_move *= -1
        self.move_speed = 0.01