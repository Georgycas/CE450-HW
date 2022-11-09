def f(suits, numbers):
    x = []

    for y in suits:
        for z in numbers:
            x.append([y, z])

    print(x)


f(['S', 'C'], [1, 2, 3])
f(['S', 'C'], [3, 2, 1])
f([], [3, 2, 1])
f(['S', 'C'], [])
