#turtle setup
import turtle as trtl
screen = trtl.Screen()
screen.bgcolor("white")
pen = trtl.Turtle()
pen.speed("fastest")

#This is the list of colors, for the spirograph.
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

#size square and coordinates
size = 800
x = 0
y = 0


for i in range(50):   #pen moves diagonally from the top left corner
    pen.up()
    pen.goto(x - size / 2, y + size / 2)
    pen.down()
    pen.color(rainbow_colors[i % len(rainbow_colors)]) #colors the squares in a pattern, based on the original list.
    for _ in range(4):  #creates the squares
        pen.forward(size)
        pen.right(90)
    size -= 16

pen.hideturtle() 
screen.mainloop() 
