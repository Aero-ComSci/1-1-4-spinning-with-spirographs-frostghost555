import turtle as trtl


screen = trtl.Screen()
screen.bgcolor("white")
pen = trtl.Turtle()
pen.speed("fastest")

size = 800
x = 0
y = 0


for i in range(50):
    pen.up()
    pen.goto(x - size / 2, y + size / 2)
    pen.down()
    
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    
    # Update size and move to the next square
    size -= 16

pen.hideturtle()  # Hide the turtle after drawing
screen.mainloop()  # Keep the window open
