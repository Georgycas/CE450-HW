def fltn(ls):
    y = []

    def sort():
        if isinstance(ls[i], list):
            print(i)
            y.append(ls[i])
        else:
            print(i)
            y.append(ls[i])
        return sort()
    sort()
    print(y)


fltn([1, 2, 3])  # normal list
x = [1, [2, 3], 4]  # deep list
fltn(x)
x = [[1, [1, 1]], 1, [1, 1]]  # deep list
fltn(x)
