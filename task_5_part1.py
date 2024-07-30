def caching_fibonacci():
    cache = {}

    def fibonacci(n):                               # Closure for fibonacci func to have an opportunity to "lock" previous calculations in cache
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:                            # Taking values from cache
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)  # Fibonacci func as it is
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))