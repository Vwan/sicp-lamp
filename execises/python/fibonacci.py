'''[Fibonacci number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        return a + b

assert fibonacci(20)== 6765