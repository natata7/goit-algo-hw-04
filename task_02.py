import turtle


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


def draw_snowflake(order):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch(t, order, 300)
        t.right(120)

    screen.mainloop()


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    draw_snowflake(level)

