def rm_all(elem, lst):
    y = []
    i = 0
    while i < len(lst):
        if lst[i] != elem:
            y.append(lst[i])
        i = i + 1
    print(y)


x = [3, 1, 2, 1, 5, 1, 1, 7]
rm_all(1, x)

