def fltn(ls):
    flat = []

    def deepchk(i=0):
        if i == len(ls):
            return
        elif type(ls[i]) is list:
            def deepflat(y=0):
                if y == len(ls[i]):
                    return deepchk(i + 1)
                elif type(ls[i][y]) is list:
                    def layer3(lr3=0):
                        if lr3 == len(ls[i][y]):
                            return deepflat(y + 1)
                        else:
                            a = ls[i][y][lr3]
                            flat.append(a)
                            return layer3(lr3 + 1)

                    layer3()

                else:
                    a = ls[i][y]
                    flat.append(a)
                    return deepflat(y + 1)

            deepflat()
        else:
            flat.append(ls[i])
            return deepchk(i + 1)

    deepchk()
    print(flat)


fltn([1, 2, 3])  # normal list
x = [1, [2, 3], 4]  # deep list
fltn(x)
x = [[1, [1, 1]], 1, [1, 1]]  # deep list
fltn(x)
