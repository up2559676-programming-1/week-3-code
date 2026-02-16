# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import tkinter
from graphix import Entry, Rectangle, Text, Window, Circle, Point


def ex1():
    win = Window("Circle Grid", 400, 400)

    radius = 20
    spacing = 60

    for row in range(5):
        y = radius + row * spacing
        fill = "blue" if row % 2 else "red"

        for col in range(5):
            x = radius + col * spacing

            circle = Circle(Point(x, y), radius)
            circle.fill_colour = fill
            circle.draw(win)

    win.get_mouse()


def ex2():
    win = Window("Click Two Corners")
    p1 = win.get_mouse()
    p2 = win.get_mouse()

    coord1 = p1.clone()
    coord1.move(0, -10)
    coord2 = p2.clone()
    coord2.move(0, 10)

    Text(coord1, f"({p1.x}, {p1.y})").draw(win)
    Text(coord2, f"({p2.x}, {p2.y})").draw(win)

    width = p2.x - p1.x
    width_point = Point(p1.x + width // 2, p1.y - 10)
    print(width_point)
    Text(width_point, f"W: {abs(width)}").draw(win)

    height = p2.y - p1.y
    height_point = Point(p1.x - 30, p1.y + height // 2)
    Text(height_point, f"H: {abs(height)}").draw(win)

    r = Rectangle(p1, p2)
    r.fill_colour = "lightblue"
    r.draw(win)

    win.get_mouse()


def ex3():
    cell = 100
    colour = "orange"
    win = Window("Ten Squares", 500, 500)

    outline_colour = Entry(Point(0, 0), 10)
    outline_colour.text = colour
    outline_colour.draw(win)

    for _ in range(10):
        p = win.get_mouse()
        top_left = Point((p.x // cell) * cell, (p.y // cell) * cell)
        bottom_right = Point(top_left.x + cell, top_left.y + cell)
        r = Rectangle(top_left, bottom_right)
        r.fill_colour = outline_colour.text or colour
        r.outline_colour = "black"
        r.draw(win)

    win.get_mouse()


def ex4():
    cell = 30
    radius = 30

    def is_valid_colour(win: Window, colour: str) -> bool:
        try:
            win.winfo_rgb(colour)
            return True
        except tkinter.TclError:
            return False

    win = Window("Click & Colour", 400, 400)
    colour_box = Entry(Point(200, 200), 10)
    colour_box.draw(win)

    for _ in range(5):
        p = win.get_mouse()
        p = Point((p.x // cell) * cell, (p.y // cell) * cell)
        c = Circle(p, radius)
        colour = colour_box.text or "grey"
        while not is_valid_colour(win, colour):
            Text(Point(200, 10), f"Invalid colour '{colour}'").draw(win)
            colour = colour_box.text or "grey"
            win.get_mouse()

        c.fill_colour = colour
        c.draw(win)

    win.get_mouse()


if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
    ex4()
