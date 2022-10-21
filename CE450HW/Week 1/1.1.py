def if_function(con, true_result, false_result):
    if con:
        print(con, end=" ")
        return true_result
    elif not con:
        print(con, end=" ")
        return false_result
    else:
        print("Not a True or False input")


print(if_function(True, 2, 3))
print(if_function(False, 2, 3))
print(if_function(3 == 2, 3 + 2, 3 - 2))
print(if_function(3 > 2, 3 + 2, 3 - 2))
