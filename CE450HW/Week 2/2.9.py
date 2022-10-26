def A(n):
    if n <= 3:
        return 3
    elif n > 3:
        return A(n-1)