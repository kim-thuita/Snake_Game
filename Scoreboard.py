from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALIGN = "center"

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.scoreboard()
        self.hideturtle()

    def scoreboard(self):
        self.write(f"Score is {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("Yellow")
        self.write("OOOPS!!GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.scoreboard()
