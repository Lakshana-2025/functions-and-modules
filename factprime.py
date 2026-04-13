def factors(n):
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list

def prime_factors(n):
    prime_factors_list = []
    i = 2
    temp = n
    while i * i <= temp:
        while temp % i == 0:
            prime_factors_list.append(i)
            temp //= i
        i += 1
    if temp > 1:
        prime_factors_list.append(temp)
    return prime_factors_list

num = int(input("Enter a number: "))

print(f"Factors of {num}:", factors(num))
print(f"Prime factors of {num}:", prime_facto
