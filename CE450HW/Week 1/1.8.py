def double_5(n):
    if n < 55:
        return False
    else:
        return n % 100 == 55 or double_5(n // 10)


print(double_5(5))
print(double_5(55))
print(double_5(55))
print(double_5(12345))
print(double_5(50505050))