n = int(input("Enter value of n: "))

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

sum_series = 0
for i in range(1, n + 1):
    sum_series += i / factorial(i)

print("Sum of the series is:", round(sum_series, 4))
