def double_5(n):
    lm = len(str(n))
    lst = list(map(int, str(n)))
    if lm > 1:
        i = 0
        while i < lm:
            if lst[i] == lst[i+1]:
                print(i)
            i = i + 1
    else:
        print("One Digit")


double_5(5)
double_5(56)

