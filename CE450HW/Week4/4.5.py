def mrg(ls1, ls2):
    ls1 = ls1 + ls2

    def rec(r=0):
        if r == len(ls1):
            return True
        else:
            def rec_sort(i=0):
                if i == len(ls1):
                    return
                else:
                    if ls1[r] < ls1[i]:
                        ls1[r], ls1[i] = ls1[i], ls1[r]
                    # code here
                    rec_sort(i + 1)

            rec_sort()
            # code here
        rec(r + 1)

    rec()  # start
    return ls1


print(mrg([1, 3, 5], [2, 4, 6]))
print(mrg([], [2, 4, 6]))
print(mrg([1, 2, 3], []))
print(mrg([5, 7], [2, 4, 6]))
