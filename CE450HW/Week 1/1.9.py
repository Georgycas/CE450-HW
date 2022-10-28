def uniq_digits(x):
    lst = list(map(int, str(x)))
    lstuniqnumbers = []
    uniqnumbers = set(lst)

    for lst in uniqnumbers:
        lstuniqnumbers.append(lst)

    print(len(lstuniqnumbers))


uniq_digits(8675309)
uniq_digits(1313131)
uniq_digits(13173131)
uniq_digits(10000)
uniq_digits(101)
uniq_digits(10)
