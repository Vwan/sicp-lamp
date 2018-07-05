def average_damping(f):
    return lambda x: (x + f(x)) / 2

f = lambda x: x*x
ad = average_damping(f)
print(ad(10))

def fixed_point(f, x):
    if abs(f(x)-x) < 0.0001:
        return x
    else:
        return fixed_point(f, f(x))

def sqrt(x):
    return fixed_point(average_damping(lambda y: x/y ), 1.0)

def cube_root(x):
    return fixed_point(average_damping(lambda y: x/(y*y) ), 1.0)

print(sqrt(4))
print(cube_root(9))