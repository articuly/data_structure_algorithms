# coding:utf-8
from turtle import *


def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(72)
        draw_spiral(t, line_len - 5)


def draw_tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(t, branch_len - 15)
        t.left(40)
        draw_tree(t, branch_len - 10)
        t.right(20)
        t.backward(branch_len)


def draw_triangle(point, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(point[0])
    t.down()
    t.begin_fill()
    t.goto(point[1])
    t.goto(point[2])
    t.goto(point[0])
    t.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, t):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, colormap[degree], t)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, t)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, t)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree - 1, t)


if __name__ == '__main__':
    t = Turtle()
    # t.left(90)
    # t.backward(100)
    screen = t.getscreen()
    # draw_spiral(t, 150)
    # draw_tree(t, 100)
    my_points = [(-300, -150), (0, 300), (300, -150)]
    sierpinski(my_points, 5, t)
    screen.exitonclick()
