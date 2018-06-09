'''[Fibonacci number - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)'''

def fibonacci(n):
    if n < 2 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
assert fibonacci(20)== 6765