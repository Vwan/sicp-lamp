def square(x):
    return x * x

def sqrt(x):
    def average_guess( y):
        return (x + y) / 2.0

    def improve_guess( guess):
        return average_guess(x / guess, guess)

    def square_iter(guess):
        good_enough = abs(square(guess) - x)
        if good_enough < 0.001:
            print("----", guess, good_enough)
            return guess
        else:
            guess = improve_guess(x, guess)
            print("++++", guess)
            square_iter(x, guess)

    return square_iter(x, 1.0)

print(sqrt(9))