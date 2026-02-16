# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from graphix import Point, Window, Line, Rectangle, Circle


def ex0():
    win_size = 600
    step = 100

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        Line(Point(x, 0), Point(x, win_size)).draw(win)

    for y in range(0, win_size, step):
        Line(Point(0, y), Point(win_size, y)).draw(win)

    win.get_mouse()


def ex1a():
    win_size = 600
    step = 100
    radius = step // 2

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        for y in range(0, win_size, step):
            circle = Circle(Point(x + radius, y + radius), radius)
            circle.fill_colour = "red"
            circle.draw(win)

    win.get_mouse()


def ex1b():
    win_size = 600
    step = 100

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        for y in range(0, win_size, step):
            rect = Rectangle(Point(x, y), Point(x + step, y + step))
            rect.fill_colour = "blue"
            rect.draw(win)

    win.get_mouse()


def ex3():
    win_size = 600
    step = 100

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        Line(Point(x, 0), Point(win_size, win_size - x)).draw(win)
        Line(Point(x, 0), Point(0, x)).draw(win)
        Line(Point(x, win_size), Point(0, win_size - x)).draw(win)
        Line(Point(x, win_size), Point(win_size, x)).draw(win)

    win.get_mouse()


def ex4():
    win_size = 600
    radius = 50
    step = radius * 2

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        for y in range(0, win_size, step):
            circle = Circle(Point(x + radius, y + radius), radius)
            circle.fill_colour = "red"
            circle.draw(win)

            if x == 0:
                Line(Point(x, y), Point(win_size, y)).draw(win)

        Line(Point(x, 0), Point(x, win_size)).draw(win)

    win.get_mouse()


def ex5():
    win_size = 600
    radius = 50
    step = radius * 2

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        Line(Point(x, 0), Point(win_size, win_size - x)).draw(win)
        Line(Point(x, 0), Point(0, x)).draw(win)
        Line(Point(x, 0), Point(x, win_size)).draw(win)
        Line(Point(x, win_size), Point(0, win_size - x)).draw(win)
        Line(Point(x, win_size), Point(win_size, x)).draw(win)

    for y in range(0, win_size, step):
        Line(Point(0, y), Point(win_size, y)).draw(win)

    win.get_mouse()


def ex6():
    win_size = 600
    step = 100
    radius = step // 2

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        for y in range(0, win_size, step):
            rect = Rectangle(Point(x, y), Point(x + step, y + step))
            rect.fill_colour = "blue"
            rect.draw(win)

            circle = Circle(Point(x + radius, y + radius), radius)
            circle.fill_colour = "red"
            circle.draw(win)

    win.get_mouse()


def ex7():
    win_size = 600
    step = 100
    radius = step // 2

    win = Window("X", win_size, win_size)

    for x in range(0, win_size, step):
        for y in range(0, win_size, step):
            rect = Rectangle(Point(x, y), Point(x + step, y + step))
            rect.fill_colour = "blue"
            rect.draw(win)

            circle = Circle(Point(x + radius, y + radius), radius)
            circle.fill_colour = "red"
            circle.draw(win)

            if x == 0:
                Line(Point(x, y), Point(win_size, y)).draw(win)

        Line(Point(x, 0), Point(x, win_size)).draw(win)

    win.get_mouse()


if __name__ == "__main__":
    ex0()
    ex1a()
    ex1b()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()
