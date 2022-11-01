# Ask the professor this weird input
def add(a, b):
    return a + b


def foo(f, n):
    def g(m):
        return f(n, m)

    return g


foo(add, 2)(1)
"""add3 = foo(incr, 5)
add3(3)
foo(triple, 5)(1)
foo(square, 2)(5)
foo(square, 4)(5)"""
