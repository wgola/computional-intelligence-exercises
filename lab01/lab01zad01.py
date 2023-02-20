def prime(n):
    if n <= 1:
        return False
    else:
        prime = True
        for i in range(2, n-1):
            if n % i == 0:
                prime = False
                break
        return prime


print(prime(3))
print(prime(4))
print(prime(49))


def select_primes(x):
    return [number for number in x if prime(number)]


print(select_primes([3, 6, 11, 25, 19]))
