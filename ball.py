from turtle import Turtle 


speedlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.xmove = 10
        self.ymove = 10
        self.penup()
        self.speed(0)
        self.color('white')
        self.shape('circle')
        self.shapesize(1, 1)
        self.timeset = 0.1

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def ybounce(self):
        self.ymove *= -1

    def xbounce(self):
        self.xmove *= -1
        self.timeset * 0.9

    def restart(self):
        self.goto(0, 0)
        self.timeset = 0.1
        self.xbounce()