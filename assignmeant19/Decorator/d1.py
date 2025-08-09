# Memoization decorator
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]  # Return cached result
        result = func(*args)   # Compute result
        cache[args] = result   # Store in cache
        return result
    return wrapper
@memoize
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the position in Fibonacci sequence: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

def fibonacci_sequence(n):
    return [fibonacci(i) for i in range(n)]

    