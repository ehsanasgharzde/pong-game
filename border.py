from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        
        # table lines
        self.speed(0)
        self.pencolor('white')
        self.hideturtle()
        self.pensize(5)

        self.penup()
        self.goto(400, 300)
        self.pendown()
        self.goto(-400, 300)

        self.penup()
        self.goto(-400, -300)
        self.pendown()
        self.goto(400, -300)
        
        self.pensize(1)

        self.penup()
        self.goto(402, 300)
        self.pendown()
        self.goto(402, -300)

        self.penup()
        self.goto(-402, 300)
        self.pendown()
        self.goto(-402, -300)

        # middle line
        self.penup()
        self.pensize(5)
        self.goto(0, 296)
        self.setheading(270)

        for _ in range (-300, 300, 20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)