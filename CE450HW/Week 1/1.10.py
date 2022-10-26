def sumOfDiv(x):
    sum = 1
    for i in range(2, x):
        if x % i == 0:
            sum += i
    return sum


def isAmicable(a, b):
    if sumOfDiv(a) == b and sumOfDiv(b) == a:
        return True
    else:
        return False


def amc(n):
    i = n + 1
    while i < 10000:
        j = 0
        while j < 10000:
            if isAmicable(i, j):
                return i
            j += 1
        i += 1


print(amc(5))
print(amc(220))
print(amc(284))
r = amc(5000)
print(r)
