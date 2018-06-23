def square(a):
    return a * a

square_lambda = lambda a: a * a

assert square(3) == square_lambda(3)


def calc_sum_of_square(a, b):
    def square(a):
        return a * a
    if a > b:
        return 0
    else:
        return square(a) + calc_sum_of_square( a+1, b)

def calc_sum_of_square_l(a, b):
    square = lambda a: a * a
    if a > b:
        return 0
    else:
        return square(a) + calc_sum_of_square( a+1, b)

print(calc_sum_of_square_l(1, 10))

print(type(lambda a: a * a))