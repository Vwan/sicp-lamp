'''[Fibonacci number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)'''
'''Iterative process'''

def fibonacci(n):
    def fib_iter(a, b, n):
        if n == 0:
            return b
        else:
            return fib_iter(a + b, a, n-1)
    return fib_iter(1, 0, n)

assert fibonacci(5) == 5

#assert fibonacci(20)== 6765