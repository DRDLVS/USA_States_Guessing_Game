from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 7, "bold")

class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.penup()
        self.hideturtle()
        self.speed(1)
        self.goto(x, y)

    def show_name(self):
        """Muestra el nombre del estado en el mapa."""
        self.write(self.name, align=ALIGNMENT, font=FONT)
