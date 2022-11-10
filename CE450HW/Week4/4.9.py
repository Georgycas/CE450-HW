from operator import add,sub,mul

print(sub(1,2))


"""Return the result of applying the function g to the initial value m     and the first element in lst, and repeatedly applying g to this result and the next element in lst until it reaches the end of the list.

    >>> s = [3, 2, 1]
    >>> fld (s, sub, 0)      	# sub(sub(sub(0, 3), 2), 1)
    -6
    >>> fld (s, add, 0)      	# add(add(add(0, 3), 2), 1)
    6
    >>> fld (s, mul, 1)      	# mul(mul(mul(1, 3), 2), 1)
    6

    >>> fld ([], sub, 100)   	# return m if s is empty
    100
    """
