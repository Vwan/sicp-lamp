def square(x):
    return x * x

def sqrt(x):
    def average_guess(x, y):
        return (x + y) / 2.0

    def improve_guess( guess):
        return average_guess(x / guess, guess)

    def good_enough(y):
        v = abs(square(y) - x)
        return (v < 0.001)

    def square_iter(guess):        
        if good_enough(guess):
            print("----", guess, good_enough)
            return guess
        else:
            guess = improve_guess(guess)
            print("++++", guess)
            square_iter(guess)
    return square_iter(1.0)

print(sqrt(9))