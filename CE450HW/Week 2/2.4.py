def foo(f, n):




    """Return the function that computes the nth application of f.
    >>>  incr(5)	       # function is to add 1 for input argument number
    6

    >>> add3 = foo (incr, 5)
    >>> add3(3)        		# Doing like: incr(incr(incr(incr(incr(3)))))
    8
    >>> foo (triple, 5)(1)  	# triple(triple(triple(triple(triple(1)))))
    243
    >>> foo (square, 2)(5) 	# square(square(5))
    625
    >>> foo (square, 4)(5) 	# square(square(square(square(5))))
    152587890625
    """
