def identity(n):
    return n


def square(n):
    return n ** 2


def adder(f1, f2):
    return f1 + f2


n = int(input("Type in the one integer"))
a1 = adder(identity(n), square(n))
print(a1)
a2 = adder(a1, identity(n))
print(a2)
a3 = adder(a1, a2)
print(a3)
