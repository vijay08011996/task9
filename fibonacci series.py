from functools import reduce

# Generating Fibonacci series using lambda function
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Generating Fibonacci series with 50 elements
result = fibonacci(50)
print(result)
