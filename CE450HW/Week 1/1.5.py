def lrgst_factor(m):
    faclist = []
    i = 1
    while i < m:
        p = m / i
        if p - int(p) == 0:
            faclist.append(i)
        i = i + 1
    print("Factors of", m, "are", faclist)
    faclist.reverse()
    print("The largest factor is : "
          + str(faclist[0]))


lrgst_factor(15)
lrgst_factor(80)
