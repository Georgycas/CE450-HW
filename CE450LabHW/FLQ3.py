def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def display_prime_number_pairs(y):
    for i in range(2, y):
        if is_prime(i) and is_prime(i + 2):
            print(f"{i}, {i + 2}")


def main():
    while True:
        x = input("Please enter a number between 10000 to 100 ")
        if x.isdigit():
            x = int(x)
            if x >= 100:
                display_prime_number_pairs(x)
                break
            else:
                print("Enter above 100")
        else:
            print("Enter a number")


main()
