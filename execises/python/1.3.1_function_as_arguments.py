def square(a):
    return a * a

def itself(a):
    return a

def sum(a, b):
    return a + b

def sum_ints(a, b):
    '''# calcualte sum of numbers in between a and b'''
    if a > b:
        return 0
    else:
        return a + sum_ints(a+1, b)

def sum_of_squares(a, b):
    '''# calcualte sum of the square of numbers in between a and b'''
    if a > b:
        return 0
    else:
        return square(a) + sum_of_squares(a+1, b)

def multiply(a, b):
    if a > b:
        return 1
    else:
        return a * multiply(a+1, b)

# print(sum(1,5))
# print(multiply(1,5))

def calc_1(f, a, b):
    '''abstract from sum and multiple functions'''
    if a > b:
        return 0
    else:
        if f.__name__ == 'multiply':
            return a * calc_1(f, a+1, b)
        elif f.__name__ == 'sum_ints':
            return a + calc_1(f, a+1, b)

def calc_2(f, a, b):
    '''abstract from itself and sum_of_squares functions'''
    if a > b:
        return 0
    else:
        return f(a) + calc_2(f, a+1, b)

print(calc_1(sum_ints, 1, 10))
print(calc_2(itself, 1, 10))
print(sum_ints(1, 10))
assert sum_ints(1,10) == calc_1(sum_ints, 1, 10) == calc_2(itself, 1, 10)

total = 0
for i in range(1, 11):
    total += square(i)
assert calc_2(square, 1, 10) == total
