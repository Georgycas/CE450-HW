def square(x):
    return x ** 2


def triple(x):
    return x ** 3


def increment(x):
    return x + 1


def identity(x):
    return x


def intscts(f, x):
    if f == x:
        return f
    else:
        return True

at_three = intscts(square, 3)
at_three(triple)

at_three(increment)
at_one = intscts(identity, 1)
at_one(square)
at_one(triple)
