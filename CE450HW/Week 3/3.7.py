def  cyc(g1, g2, g3):

    def add_one(x):
    return x + 1

    def times_two(x):
    return x * 2

    def add_three(x):
    return x + 3

    my_cyc = cyc(add_one, times_two, add_three)
    h= my_cyc(0)
    h(5)

    h = my_cyc(2)
    h(1)

    h = my_cyc(3)
    h(2)

    h = my_cyc(4)
    h(2)

    h = my_cyc(6)
    h(1)
