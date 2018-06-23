def square(x):
    return x * x

def sqrt(x, guess):

    good_enough = abs(square(guess) - x)
    if good_enough < 0.001:
        print("----", guess, good_enough)
        return guess
    else:
        guess = (x / guess + guess) / 2
        print("++++", guess)
        sqrt(x, guess)

    return guess


print(sqrt(9, 1.0))