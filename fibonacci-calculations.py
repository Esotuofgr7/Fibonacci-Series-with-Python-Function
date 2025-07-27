def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
        return fib_series

# 👇 Ask the user for input and display the result
terms = int(input("Enter the number of terms: "))
print("Fibonacci series up to", terms, "terms:")
print(fibonacci(terms))
