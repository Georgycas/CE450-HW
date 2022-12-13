def verify_add(m, ls):
    s = set(ls)
    for x in s:
        if x != m and (m - x) in s:
            return True
    return False


print(verify_add(100, [1, 2, 3, 4, 5]))
print(verify_add(7, [1, 2, 3, 4, 2]))
print(verify_add(10, [5, 5]))
print(verify_add(151, range(0, 200000, 3)))
print(verify_add(50004, range(0, 200000, 4)))
