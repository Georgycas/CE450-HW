def cal(n):
    if n == 0 or n == 1:
        return n
    return n * cal(n - 2)


print(cal(5))

print(cal(8))
