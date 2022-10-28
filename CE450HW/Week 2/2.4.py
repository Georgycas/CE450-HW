def foo(f, n):
    if f == 'incr':
        return lambda a: a + 1




add3 = foo(incr, 5)
add3(3)
foo(triple, 5)(1)
foo(square, 2)(5)
foo(square, 4)(5)

