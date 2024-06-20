from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT =180
RIGHT = 0

class Snake:
    
    def __init__(this):
        this.starting_position = STARTING_POSITIONS
        this.segments = []
        this.create_snake()
        this.snake_head = this.segments[0]
    
    def create_snake(this):
        for position in this.starting_position:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            this.segments.append(new_segment)
        
    def move(this):
        for seg_num in range(len(this.segments) - 1, 0, -1):
            new_x = this.segments[seg_num - 1].xcor()
            new_y = this.segments[seg_num - 1].ycor()
            this.segments[seg_num].goto(new_x, new_y)
        this.snake_head.forward(MOVE_DISTANCE)

    def up(this):
        if this.snake_head.heading() != DOWN:
            this.snake_head.setheading(UP)

    def down(this):
        if this.snake_head.heading() != UP:
            this.snake_head.setheading(DOWN)

    def left(this):
        if this.snake_head.heading() != RIGHT:
            this.snake_head.setheading(LEFT)

    def right(this):
        if this.snake_head.heading() != LEFT:
            this.snake_head.setheading(RIGHT)
    