def same_ord(a, b):
    if len(str(a)) == len(str(b)):
        print("True")
        print(len(str(a)), "bits of a and b")

    else:
        print("False")
        print(a, "is", len(str(a)), "bits", end="; ")
        print(b, "is", len(str(b)), "bits")


same_ord(50, 70)
same_ord(50, 100)
same_ord(1000, 100000)
