def greatest_common_divisor(a, b):
    min = a
    if a > b:
        min = b
    divisor = 1
    for i in range(1, min):
        if a % i == b % i == 0:
            divisor = i
    return divisor

def greatest_common_devisior_new(a, b):
    if b == 0:
        return a
    return greatest_common_devisior_new(b, a % b)

print(greatest_common_devisior_new(28, 16))
print(greatest_common_devisior_new(16, 28))
assert greatest_common_divisor(16, 28) == greatest_common_devisior_new(16, 28)