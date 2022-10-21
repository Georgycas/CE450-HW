def    smth(g, dx):
   f(x) = (g(x - dx) + g(x) + g(x + dx)) / 3
    square = lambda x: x ** 2
    round(smth(square, 1)(0), 3)
