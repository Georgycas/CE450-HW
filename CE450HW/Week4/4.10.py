def crte_2d_arr(rows, columns):
    x = []
    n = []

    def col(z, i=0):
        if i == z:
            return
        else:
            x.append('_')
        col(z, i + 1)

    def row(z, i=0):
        if z == i:
            return
        else:
            n.append(x)
        row(z, i + 1)

    col(columns)
    row(rows)
    return n


print(crte_2d_arr(3, 5))
