from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.refresh_score()
        
    
    def refresh_score(self):
        """Shows level on the screen."""
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}",align="center",font=FONT)

    def game_over(self):
        """Tells when the game is over."""
        self.goto(-50,0)
        self.write(arg="Game Over",align="left",font=FONT)
