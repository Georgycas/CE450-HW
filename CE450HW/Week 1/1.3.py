def sum(a, b):
    sum = a ** 2 + b ** 2
    print(sum)


def foo(a, b, c, d):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if a > c:
        a, c = c, a
    if d < b:
        d, b = b, d
    sum(a, b)


foo(1, 2, 3, 4)
foo(-3, 1, 5, 6)
