from graphix import Window, Point, Circle, Line, Text


def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)


def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    arms = Line(Point(150, 180), Point(250, 180))
    arms.draw(win)
    right_leg = Line(Point(200, 240), Point(250, 300))
    right_leg.draw(win)
    left_leg = Line(Point(200, 240), Point(150, 300))
    left_leg.draw(win)

    win.get_mouse()


def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()


# Solutions below:
