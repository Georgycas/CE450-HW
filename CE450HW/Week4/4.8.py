def check(b, n=0):
    c = True

    if len(b) == n:
        print(c)
        return True

    if b[n] != b[-1 - n]:
        print(False)
        return False

    check(b, n + 1)


def sym(l):
    if not l:
        print(True)
    else:
        check(l)


sym([])
sym([1])
sym([1, 4, 5, 1])
sym([1, 4, 4, 1])
sym(['l', 'o', 'l'])
