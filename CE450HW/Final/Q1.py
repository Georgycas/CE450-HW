def trc1(f):
    def wrapper(*args, **kwargs):
        print(f"Calling {f} on arguments {args}")
        result = f(*args, **kwargs)
        print(result)
        return result
    return wrapper


@trc1
def sqr(x):
    return x * x


@trc1
def sum_sqr(n):
    return sum(sqr(i) for i in range(1, n + 1))


sqr(3)
sum_sqr(3)
