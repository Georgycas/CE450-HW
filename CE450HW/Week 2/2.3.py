def is_Prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


def cnt_primes(m):
    i = 0
    cntprime = 0
    while i < m:
        if is_Prime(i):
            cntprime = cntprime + 1
        i += 1
    return cntprime


print(cnt_primes(6))
