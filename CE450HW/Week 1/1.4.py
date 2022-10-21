def df(x, y, z):
    if x > y:
        x, y = y, x

    if x > z:
        x, z = z, x

    if y > z:
        y, z = z, y

    if z - y == x:
        print("True", z, "-", y, "=", x)

    else:
        print("False", z, "-", y, "does not =", x)


df(5, 3, 2)
df(2, 3, 5)
df(2, 5, 3)
df(-2, 3, 5)
df(-5, -3, -2)
df(-2, 3, -5)
df(2, 3, -5)
df(10, 6, 4)
df(10, 6, 3)
