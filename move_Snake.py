from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self,):
        self.segment = []
        self.snake()
        self.head = self.segment[0]

    def snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self,positions):
        old_segment = Turtle("square")
        old_segment.color("white")
        old_segment.penup()
        old_segment.goto(positions)
        self.segment.append(old_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x_axis = self.segment[seg_num - 1].xcor()
            y_axis = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x_axis, y_axis)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
         self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
           self.head.setheading(LEFT)







