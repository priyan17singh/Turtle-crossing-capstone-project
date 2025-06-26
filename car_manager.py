from turtle import Turtle
import random,time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 10
        self.all_cars = []
        self.hideturtle()
    

    def create_car(self):
        """Creates a new cars."""
        random_choice = random.randint(1,5)
        if random_choice == 1 :
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)



    def move_cars(self):
        """Moves the car with a constant speed towards left."""
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def reset_car_speed(self):
        """Increases the speed of car."""
        self.car_speed += 5

    def collision(self , player):
        """Checks collision with turtle."""
        for car in self.all_cars:
            if player.distance(car) <=30 :
                return True
        
       
