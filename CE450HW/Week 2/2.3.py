def cnt_primes(m):
    if is_prime(m):
        return 1 + cnt_primes(m - 1)
    else:
        return cnt_primes(m - 1)

print(cnt_primes(6))
