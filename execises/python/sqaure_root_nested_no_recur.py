def square(x):
    return x * x

def sqrt(x):
    def average_guess(x, y):
        return (x + y) / 2.0

    def improve_guess( y):
        return average_guess(x / y, y)

    def good_enough(y):
        v = abs(square(y) - x)
        return (v < 0.001)

    guess = 1
    while not good_enough(guess):
        guess = improve_guess( guess)
        print("++++", guess)
    return guess

print(sqrt(9))