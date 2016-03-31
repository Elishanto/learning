import math


def primes(n):
    a = [True] * n

    for i in range(2, int(math.sqrt(n))):
        for j in range(i * 2, n, i):
            a[j] = False
    return [i for i in range(2, n) if a[i]]


print(primes(int(input())))
