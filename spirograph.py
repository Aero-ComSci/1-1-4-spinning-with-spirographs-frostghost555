import turtle as trtl
screen = trtl.Screen()
screen.bgcolor("white")
pen = trtl.Turtle()
pen.speed("fastest")

size = 800
x = -400
y = 400
origin=(x, y)

for i in range(50):
    pen.up()
    x = x + 8
    y = y - 8
    size = size - 16
    pen.down()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
        
pen.hideturtle()
screen.mainloop()
