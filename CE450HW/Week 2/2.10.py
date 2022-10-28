def bnc_bck_frth(k):
    A = []
    B = 1
    trace = 1
    for I in range(1, 101):
        if I % 7 == 0 or '7' in str(I):
            trace = trace * -1
        if trace == 1:
            A.append(B)
            B += 1
        else:
            A.append(B)
            B -= 1
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
