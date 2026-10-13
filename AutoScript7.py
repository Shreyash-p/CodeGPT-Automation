# This script demonstrates the use of the LRU cache decorator from the functools module to cache the results of expensive function calls.

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """Return the n-th Fibonacci number using memoization."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function with some predefined values
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(5))  # Output: 5
print(fibonacci(10)) # Output: 55