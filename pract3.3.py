# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from math import sqrt

from graphix import Circle, Entry, Line, Point, Rectangle, Text, Window


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


def draw_circle():
    radius = int(input("Enter the radius: "))

    win = Window()
    Circle(Point(win.width // 2, win.height // 2), radius).draw(win)

    win.get_mouse()


def draw_archery_target():
    margin = 20

    win = Window()
    width = win.width
    height = win.height

    centre = Point(width // 2, height // 2)

    blue_rad = height // 2 - margin
    yellow_rad = blue_rad // 3
    red_rad = yellow_rad * 2

    blue = Circle(centre, blue_rad)
    blue.fill_colour = "blue"
    blue.draw(win)
    red = Circle(centre, red_rad)
    red.fill_colour = "red"
    red.draw(win)
    yellow = Circle(centre, yellow_rad)
    yellow.fill_colour = "yellow"
    yellow.draw(win)

    win.get_mouse()


def blue_circle():
    radius = 100

    win = Window()
    centre = win.get_mouse()
    cirle = Circle(centre, radius)
    cirle.fill_colour = "blue"
    cirle.draw(win)

    win.get_mouse()


def ten_lines():
    win = Window()

    for _ in range(10):
        p1 = win.get_mouse()
        p2 = win.get_mouse()
        Line(p1, p2).draw(win)


def ten_strings():
    win = Window()

    entry = Entry(Point(50, 15), 10)
    entry.draw(win)

    for _ in range(10):
        anchor = win.get_mouse()
        Text(anchor, entry.text).draw(win)

    win.get_mouse()


def ten_coloured_rectangles():
    win = Window()

    entry = Entry(Point(50, 15), 10)
    entry.text = "blue"
    entry.draw(win)

    for _ in range(10):
        p1 = win.get_mouse()
        p2 = win.get_mouse()
        rect = Rectangle(p1, p2)
        rect.fill_colour = entry.text or "blue"
        rect.draw(win)


def five_click_stick_figure():
    win = Window()

    def dist_two_points(p1: Point, p2: Point) -> float:
        x = abs(p1.x - p2.x) ** 2
        y = abs(p1.y - p2.y) ** 2

        return sqrt(x + y)

    head_centre = win.get_mouse()
    head_outer = win.get_mouse()
    head_radius = int(dist_two_points(head_centre, head_outer))
    Circle(head_centre, head_radius).draw(win)

    body = win.get_mouse()
    Line(
        Point(head_centre.x, head_centre.y + head_radius), Point(head_centre.x, body.y)
    ).draw(win)

    arms = win.get_mouse()
    arm_dist = abs(arms.x - head_centre.x)
    Line(
        Point(head_centre.x - arm_dist, arms.y), Point(head_centre.x + arm_dist, arms.y)
    ).draw(win)

    legs = win.get_mouse()
    leg_dist = abs(legs.x - head_centre.x)
    Line(Point(head_centre.x, body.y), Point(head_centre.x - leg_dist, legs.y)).draw(
        win
    )
    Line(Point(head_centre.x, body.y), Point(head_centre.x + leg_dist, legs.y)).draw(
        win
    )

    win.get_mouse()


if __name__ == "__main__":
    # draw_stick_figure()
    # draw_circle()
    # draw_archery_target()
    # blue_circle()
    # ten_lines()
    # ten_strings()
    # ten_coloured_rectangles()
    five_click_stick_figure()
