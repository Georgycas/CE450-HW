def mrg(ls1, ls2):
    ls1 = ls1 + ls2
    sort_ls = []
    r = 0
    def rec(r):
        if len(ls1) == len(sort_ls):
            return sort_ls
        else:
            def rec_sort(i=0):
                if r == i:
                    return sort_ls
                else:
                    if ls1[r] < ls1[i]:
                        sort_ls.append(i)
                rec_sort(i + 1)
        rec(r + 1)
    rec()


print(mrg([1, 3, 5], [2, 4, 6]))
print(mrg([], [2, 4, 6]))
print(mrg([1, 2, 3], []))
print(mrg([5, 7], [2, 4, 6]))
