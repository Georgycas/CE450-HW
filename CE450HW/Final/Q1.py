"""Write a function as a decorator of other function calls for the following
operations
def  trc1(g):
 YOUR SOURCE CODE HRER
@trc1
def  sqr(x):
    return x*x
@trc1
def  sum_sqr(n):
 YOUR SOURCE CODE HRER
sqr(3)
Calling <function sqr at 0x7f73e7ce8620> on argument 3
9 # 9 = 3^2
sum_sqr(3)
Calling <function sum_sqr at 0x7f73e7c410d0> on argument 3
Calling <function sqr at 0x7f73e7c41158> on argument 1
Calling <function sqr at 0x7f73e7c41158> on argument 2
Calling <function sqr at 0x7f73e7c41158> on argument 3
14 # 14 = 1^2 + 2^2 + 3^2 """


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
