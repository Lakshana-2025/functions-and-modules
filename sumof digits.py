def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(int(n / 10))

number_input = input("Enter a number: ")
number = abs(int(number_input))
result = sum_digits(number)
print(result)
