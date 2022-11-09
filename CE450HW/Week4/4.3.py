def add_many(x, elem, lt):
    i = 0
    while i < x:
        lt.append(elem)
        i += 1


lst = [1, 2, 4, 2, 1]
add_many(2, 5, lst)
print(lst)
