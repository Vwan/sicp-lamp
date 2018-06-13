def square(x):
    return x * x

def exponent(x, n):
    if n == 0:
        return 1
    else:
        return x * exponent(x, n-1)

def exponent_improved(x, n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return square(exponent_improved(x, n/2))
    else:
        return x * exponent_improved(x, n-1)

def exponent_improved_further(x, n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return square(exponent_improved(x, n/2))
    else:
        return x * square(exponent_improved(x, (n-1)/2))

print(exponent(2, 100))
print(exponent_improved(2, 100))

print(exponent_improved_further(2, 100))