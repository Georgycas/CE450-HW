def sumDiv(x):
    sum = 1
    for i in range(2, x):
        if x % i == 0:
            sum = sum + i
    return sum


def isAmc(a, b):
    if sumDiv(a) == b and sumDiv(b) == a:
        return True
    else:
        return False


def amc(n):
    Num = n + 1
    while Num < 6000:
        count = 0
        while count < 6000:
            if isAmc(Num, count):
                return Num
            count = count + 1
        Num = Num + 1


print(amc(142))
print(amc(220))
print(amc(284))
r = amc(1184)
print(r)
