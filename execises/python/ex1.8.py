def cube(x):
    return x * x * x

def square(x):
    return x * x

def cube_root(x):

    def improve_guess( y):
        return (x/square(y) + 2 * y) / 3

    def good_enough(guess):
        v = abs(cube(guess) - x)
        return v < 0.001

    def cube_iter(guess):
        if good_enough(guess):
            print("----", guess, good_enough)
            return guess
        else:
            guess = improve_guess(guess)
            print("++++", guess)
            cube_iter(guess)

    return cube_iter(1.0)

print(cube_root(9))