from math import sqrt


def is_sqrt(seq):
    prfctsqrt = []
    for i in range(len(seq)):
        sq_root = int(sqrt(seq[i]))
        check = seq[i]
        if (sq_root * sq_root) == check:
            prfctsqrt = seq[i] + prfctsqrt

    return prfctsqrt


seq = [49, 8, 2, 1, 102]
print(is_sqrt(seq))
seq = [500, 30]
print(is_sqrt(seq))
