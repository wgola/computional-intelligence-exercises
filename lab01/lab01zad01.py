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


def select_primes(x):
    return [number for number in x if prime(number)]


select_primes([3, 6, 11, 25, 19])
