def chk_elm(lst, n):
    def check0(g=0):
        if g == len(lst):
            return
        elif type(lst[g]) is list:
            print("its a list")

            check0(g + 1)

        else:
            print(a[g])
            check0(g+1)

    check0()


a = [[1, [2]], 3, [[4], [5, [6]]]]
chk_elm(a, 6)
