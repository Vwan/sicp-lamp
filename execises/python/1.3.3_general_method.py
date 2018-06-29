def fx(f, a, b):
    avg = (a + b)/2
    if abs(a - b) < 0.001:
        return avg
    else:
        if f(avg) > 0:
            return fx(f, a, avg)
        elif f(avg) < 0:
            return fx(f, avg, b)
        else:
            return avg

def half_interval(f, a, b):
    a_value = f(a)
    b_value = f(b)
    if a_value < 0 and b_value > 0:
        return fx(f, a, b)
    elif b_value < 0 and a_value > 0:
        return fx(f, b, a)
    else:
        print(f"error, {a} and {b} are not of opossite sign")

formula = lambda x: x * x * x - 2 * x - 3
value = half_interval(formula, 1, 2)
print(value)