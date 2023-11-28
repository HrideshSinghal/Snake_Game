from turtle import Turtle
P = -0


class Snake:


    def __init__(self):
        self.snakes = []
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            self.add_segment(i)


    def add_segment(self, position):
        global P
        head = Turtle("square")
        head.penup()
        head.color("white")
        head.goto(P, 0)
        head.speed("fastest")
        P -= 20
        self.snakes.append(head)

    def extend(self):
        self.add_segment(self.snakes[-1])

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            xpos = self.snakes[i - 1].xcor()
            ypos = self.snakes[i - 1].ycor()
            self.snakes[i].goto(xpos, ypos)
        self.snakes[0].forward(20)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)








