def conti():
    c = input("Type yes or no to continue ")
    if c.lower() == 'yes':
        start()
    elif c.lower() == 'no':
        exit()
    else:
        c = input('Incorrect type yes or no ')
        conti()


def sum_check(sum, n):
    if sum > n:
        print(sum, ">", n)
        print("The sum of proper divisions is greater than the divisor")
        conti()
    elif sum == n:
        print(sum, "=", n)
        print("The sum of proper divisions is equal to the divisor")
        c = input("Type yes or no to continue ")
        conti()
    else:
        print(n, ">", sum)
        print("The sum of proper divisions is lesser than the divisor")
        conti()


def divisor(n):
    i = 1
    sum = 0
    while i < n:
        p = n / i
        if p - int(p) == 0:
            print(int(p), "*", i, " =", n)
            sum = sum + i
        i = i + 1
    sum_check(sum, n)


def start():
    goodinput = False
    while not goodinput:
        try:
            n = int(input('Enter a number: '))
            if n > 0:
                goodinput = True
                divisor(n)
            else:
                print("that's not a positive number. Try again: ")
        except ValueError:
            print("that's not an integer. Try again: ")


start()
