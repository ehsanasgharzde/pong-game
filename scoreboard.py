from turtle import Turtle


alignment = 'center'
font = ('Courier', 40, 'bold')
welcomefont = ('Courier', 40, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.leftscore = 0
        self.rightscore = 0
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color('white')
        self.updatescoreboard()
    
    def welcome(self):
        self.goto(0, 350)
        self.write('Welcomg to Pong!', False, alignment, welcomefont)       

    def updatescoreboard(self):
        self.clear()

        self.goto(-30, 230)
        self.write(f'{self.leftscore}', False, alignment, font)

        self.goto(30, 230)
        self.write(f'{self.rightscore}', False, alignment, font)
        

    def leftpoint(self):
        self.leftscore += 1
        self.updatescoreboard()

    def rightpoint(self):
        self.rightscore += 1
        self.updatescoreboard()
             
    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, alignment, font)