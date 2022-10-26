def bnc_bck_frth(k):
    A = []
    j = 1
    flag = 1
    for i in range(1, 101):
        if i % 7 == 0 or '7' in str(i):
            flag = flag * -1
        if flag == 1:
            A.append(j)
            j += 1
        else:
            A.append(j)
            j -= 1

    return A[k - 1]


print(bnc_bck_frth(7))
print(bnc_bck_frth(8))
print(bnc_bck_frth(15))
print(bnc_bck_frth(21))
print(bnc_bck_frth(22))
print(bnc_bck_frth(30))
print(bnc_bck_frth(68))
print(bnc_bck_frth(69))
print(bnc_bck_frth(70))
print(bnc_bck_frth(71))
print(bnc_bck_frth(72))
print(bnc_bck_frth(100))
