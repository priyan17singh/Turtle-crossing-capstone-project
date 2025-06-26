from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.refresh_player()
        
    def move_player(self):
        """Moves the player by 10px."""
        self.forward(MOVE_DISTANCE)
    
    def refresh_player(self):
        """Moves the player to starting position."""
        self.goto(STARTING_POSITION)
        
