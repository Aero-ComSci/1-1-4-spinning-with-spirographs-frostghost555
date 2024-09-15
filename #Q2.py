import turtle

#assign rectangle variables
window_width = 800
window_height = 600
rect_width = 100
rect_height = 50
num_rects = 5
shift_down = 200

#pen moves to bottom left, starts drawing
def draw_rectangle(t, x, y, width, height):
    t.penup()
    t.goto(x - width // 2, y - height // 2)
    t.pendown()
    t.setheading(0)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def main():
    #drawing window
    screen = turtle.Screen()
    screen.setup(width=window_width, height=window_height)
    screen.title("#Q2, 5 centered objects")
    screen.bgcolor("white")

    #pen properties
    t = turtle.Turtle()
    t.color("blue")
    t.speed(0)

    #rectangle spacing
    total_width = num_rects * rect_width
    total_spacing = window_width - total_width
    spacing = total_spacing // (num_rects + 1)
    
    #rectangle's position
    start_x = -window_width // 2 + spacing + rect_width // 2
    start_y = (window_height // 2 - rect_height // 2) - shift_down

    #draws rectangles
    for i in range(num_rects):
        x = start_x + i * (rect_width + spacing)
        y = start_y
        draw_rectangle(t, x, y, rect_width, rect_height)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
