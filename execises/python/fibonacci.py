'''[Fibonacci number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(20)== 6765