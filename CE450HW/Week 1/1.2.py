def sum_odd(x):
    i = abs(x)
    count = 1
    sum = 1
    while i > sum:
        count = count + 2
        sum = sum + count
    print("The sum of all odd number less than", x, "is", sum)


def start():
    goodinput = False
    while not goodinput:
        try:
            x = int(input('Enter a number: '))
            if x / 2 != int:
                goodinput = True
                sum_odd(x)
            else:
                print("that's not an odd number. Try again: ")
        except ValueError:
            print("that's not an integer. Try again: ")


start()
