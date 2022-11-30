def fancy_printing(n):
    def rep(x):
        b = 0
        while x > b:
            if b == 0:
                print(b)
                b = b + 1
            elif n % b == 0:
                print("Buzz!")
                b = b + 1
            else:
                print(b)
                b = b + 1

    return rep


replace = fancy_printing(5)
replace(10)
