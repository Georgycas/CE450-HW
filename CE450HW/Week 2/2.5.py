def op(a, b, c):
    if a == 0 or b == 0:
        return c
    if a - 1 == 0:
        return b + c
    return b + op(a - 1, b, c)


print(op(2, 4, 3))
print(op(0, 3, 2))
print(op(3, 0, 2))
