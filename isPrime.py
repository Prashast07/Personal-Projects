def is_prime(a):
    return all(a % i for i in xrange(2, a))

print is_prime(9)