def chk_elm(lst, n):
    def chx(y):
        if y == n:
            print(True)
            exit()

    def check3(dig, b=0):
        if b == len(dig):
            return
        elif type(dig[b]) is list:
            chx(dig[b])
            check3(dig, b + 1)
        else:
            chx(dig[b])
            check3(dig, b + 1)

    def check2(dig, b=0):
        if b == len(dig):
            return
        elif type(dig[b]) is list:
            check3(dig[b])
            check2(dig, b + 1)
        else:
            chx(dig[b])
            check2(dig, b + 1)

    def check1(dig, b=0):
        if b == len(dig):
            return
        elif type(dig[b]) is list:
            check2(dig[b])
            check1(dig, b + 1)
        else:
            chx(dig[b])
            check1(dig, b + 1)

    def check0(dig, b=0):
        if b == len(dig):
            return
        elif type(dig[b]) is list:
            check1(dig[b])
            check0(dig, b + 1)
        else:
            chx(dig[b])
            check0(dig, b + 1)

    check0(lst)
    print(False)


a = [[1, [2]], 3, [[4], [5, [6]]]]
chk_elm(a, 6)
