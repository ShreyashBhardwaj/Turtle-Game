from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score=0
        # self.color("black")
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.write(f"Level: {self.current_score}",False,align='center',font=FONT)

    def update(self):
        self.clear()
        self.current_score+=1
        self.write(f"Level: {self.current_score}",False,align='center',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center',font=FONT)
