from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        
        self.upspeed = 20
        self.downspeed = 20
        self.penup()
        self.speed(0)
        self.color('white')
        self.shape('square')
        self.shapesize(1, 5)
        self.setheading(90)
        
        if position == 'leftplayer':
            self.goto(-370, 0)
        elif position == 'rightplayer':
            self.goto(370, 0)

    def up(self):
        self.setheading(90)
        self.forward(self.upspeed)

        if self.ycor() > 239:
            self.upspeed = 0
        else:
            self.upspeed = 20

    def down(self):
        self.setheading(270)
        self.forward(self.downspeed)

        if self.ycor() < -239:
            self.downspeed = 0
        else:
            self.downspeed = 20