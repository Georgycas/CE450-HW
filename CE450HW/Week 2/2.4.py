def incr(a):
    return a + 1


def square(a):
    return a ** 2


def triple(a):
    return a * 3


def foo(f, n=1):
    def g(m):
        count = 1
        x = f(m)
        while count < n:
            count = count + 1
            x = f(x)
        return x

    return g


print(incr(5))
add3 = foo(incr, 5)
print(add3(3))
print(foo(triple, 5)(1))
print(foo(square, 2)(5))
print(foo(square, 4)(5))
