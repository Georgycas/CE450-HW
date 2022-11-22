from math import sqrt


def is_sqrt(seq):
    end = []
    for i in range(len(seq)):
        sq_root = int(sqrt(seq[i]))
        check = seq[i]
        if (sq_root * sq_root) == check:
            end.append(check)

    return end


seq = [49, 8, 2, 1, 102]
print(is_sqrt(seq))
seq = [500, 30]
print(is_sqrt(seq))
