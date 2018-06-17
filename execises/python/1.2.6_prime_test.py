#```最傻瓜式的```
def is_prime_silly(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

#```find the smallest divisor, if it's not the number itself, then it is a prime```
def is_prime_by_smallest_divisor(a):
    def find_divisor(a, testor):
        if testor * testor > a:
            return a
        if a % testor == 0:
            return testor
        else:
            return find_divisor(a, testor+1)
    if a == find_divisor(a, 2):
        return True
    else:
        return False

for i in range(2,10000):
    print(i, is_prime_silly(i), is_prime_by_smallest_divisor(i))
    assert is_prime_by_smallest_divisor(i) == is_prime_silly(i)

