def mk_wd(balance):
    x = balance

    def r(m):
        nonlocal x
        x = x - m
        if x > 0:
            print(x)
        else:
            print("Insufficient funds")
        return m
    return r


rem = mk_wd(100)
rem(10)
rem(20)
rem(100)
