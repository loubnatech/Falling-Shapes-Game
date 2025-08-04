from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("orange")
        self.hideturtle()
        self.goto(0,250)
        self.score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"SCORE :{self.score}",font=("courier",30,"normal"),align="center")
    def incresse_score(self,point):
        self.score+=point
        self.update_score()
    def reset_score(self):
        self.score=0
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",font=("courier",40,"normal"),align="center")