def pfct_check(sum, n):
    if sum == n:
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")


def factor_num(n):
    i = 1
    sum = 0
    while i < n:
        p = n / i
        if p - int(p) == 0:
            sum = sum + i
        i = i + 1
    pfct_check(sum, n)


factor_num(6)
factor_num(8)
factor_num(28)