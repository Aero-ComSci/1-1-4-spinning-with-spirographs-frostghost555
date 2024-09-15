import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1

while True:
  while (x < 200):

    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1
    

    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1

  # Move to the starting position of the second pattern without drawing
  painter.penup()
  x = -200
  y = 0
  move_x = 1
  move_y = -1
  painter.goto(x, y)
  painter.pendown()

  while (x < 200):

    while (y > -100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1
    

    while (y < 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1

  # Reset the position and direction for the next iteration
  painter.penup()
  x = -200
  y = 0
  move_x = 1
  move_y = 1
  painter.goto(x, y)
  painter.pendown()

wn = trtl.Screen()
wn.mainloop()
