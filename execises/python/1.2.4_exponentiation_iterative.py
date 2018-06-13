# def exponent(x, n):
#     def iter(x, n):
#         if n == 0:
#             return 1
#         else:
#             return x * iter(x, n-1)
#     return iter(x, n)

def _exponent(x, n):
    def iter(x, counter, product):
        if counter == 0:
            return product
        else:
            return iter(x, counter-1, product * x)
    return iter(x, n, 1)

#print(exponent(2, 5))
print(_exponent(2, 5))

