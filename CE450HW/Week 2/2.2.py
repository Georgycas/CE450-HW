def sum_num(n):
    if n == 0 or n == 1:
        return n
    return n + sum_num(n - 2)


print(sum_n(4))

print(sum_n(5))
