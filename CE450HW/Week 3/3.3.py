from operator import add, neg


def combine_funcs(op):
    def combined(f, g):
        def val(x):
            return op(f(x), g(x))

        return val

    return combined


add_func = combine_funcs(add)

h = add_func(abs, neg)

print(h(-5))
