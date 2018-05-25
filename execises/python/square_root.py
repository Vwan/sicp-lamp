
def average_guess(x, y):
	return (x + y) / 2.0

def improve_guess(x, guess):
	return average_guess(x / guess, guess)

def square(x):
    return x * x
    
def square_iter(x, guess):    
    good_enough = abs(square(guess) - x) 
    if good_enough < 0.001:
        print("----",guess, good_enough)
        return guess
    else:
        guess = improve_guess(x, guess)
        print("++++", guess)
        square_iter(x, guess)


def sqrt(x):
    return square_iter(x, 1.0)

print(sqrt(9))