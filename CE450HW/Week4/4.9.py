from operator import add, sub, mul


def fld(lst, g, m):
    if not lst:
        return m
    else:
        def math(c, y=0):
            if lst[y] == lst[-1]:
                return g(c, lst[y])
            else:
                return math(g(c, lst[y]), y + 1)

        return math(m)


s = [3, 2, 1]
print(fld(s, sub, 0))  # sub(sub(sub(0, 3), 2), 1)
print(fld(s, add, 0))  # add(add(add(0, 3), 2), 1)
print(fld(s, mul, 1))  # mul(mul(mul(1, 3), 2), 1)
print(fld([], sub, 100))  # return m if s is empty

s = [4, 5, 6]
print(fld(s, sub, 0))
print(fld(s, add, 0))
print(fld(s, mul, 1))
print(fld([], sub, 100))
