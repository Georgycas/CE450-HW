def A(n):
    if n <= 3:
        return n
    elif n > 3:
        return A(n - 1) + 2 * A(n - 2) + 3 * A(n - 3)


print(A(1))
print(A(2))
print(A(3))
print(A(4))
print(A(5))
print(A(6))
