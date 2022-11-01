# Ask the professor this weird input
def incr(x):
    return x + 1


def foo(f):
    func = str(f)
    if func == "incr":
        return incr()


foo(incr, 2)(1)
"""add3 = foo(incr, 5)
add3(3)
foo(triple, 5)(1)
foo(square, 2)(5)
foo(square, 4)(5)"""
