import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_sum_of_primes(n):
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(f"{n} can be expressed as the sum of {i} and {n - i}")
            return True
    print(f"{n} cannot be expressed as a sum of two prime numbers.")
    return False

num = int(input("Enter a number: "))
check_sum_of_primes(num)
