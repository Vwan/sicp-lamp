import math
def fixed_point(f, x):
    #print("--x---", x)
    if abs(f(x)-x) < 0.0001:
        return x
    else:
        #print("++f(x)+++", f(x))
        return fixed_point(f, f(x))

print(fixed_point(math.cos, 1.0))

def average(x, y):
    return (x + y) / 2

def sqrt(x):
    return fixed_point(lambda y: average(y, x/y), x)

print(sqrt(2))