def checking(x):
    if x < 10:
        return True
    y = list(map(int, str(x)))
    for i in range(len(y) - 1):
        if y[i] > y[i + 1]:
            return False
    return True


print(checking(5))
print(checking(11))
print(checking(127))  # 1<2<7
print(checking(1357))  # 1<3<5<7
print(checking(21))
print(checking(1375))
