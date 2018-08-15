
def is_prime(a):
    """
    find the smallest divisor, if it's not the number itself, then it is a prime
    :param a:
    :return:
    """
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

def prime_sum(n):
    result = []
    """
    Given a positive integer n, find all ordered pairs of distinct positive
    integers i and j, where 1 ≤ j < i ≤ n, such that i + j is prime

    :param n: positive integer
    :return: list
    """

    for i in range(1,n+1):
        for j in range(i+1, n+1):
            print( i, j, i+j)
            print("*" * 4, is_prime(i + j))
            if is_prime(i + j):
                result.append((i, j))
    return result

result = prime_sum(6)
print(result)

def prime_sum_refined(n):

    """
    Given a positive integer n, find all ordered pairs of distinct positive
    integers i and j, where 1 ≤ j < i ≤ n, such that i + j is prime
    This time make it more modular

    :param n: positive integer
    :return: list
    """

    # generate a list containing all the possible pair of (i,j) where i<j<=n
    def generate_pairs(n):
        result = []
        lx = range(1, n+1)
        ly = lambda i: range(i+1, n+1)
        for x in lx:
            for y in ly(x):
                result.append((x, y))
        return result

    # filter out if x+y is prime
    def filter_prime_pairs(result):
        final_result = []
        for i in range(len(result)): # for res in result is inifinit loop, why?
            res = result[i]
            x, y = res
            print(x, y, is_prime(x+y))
            if is_prime(x+y):
                final_result.append(res)
                print("-----", final_result)
        return final_result

    return filter_prime_pairs(generate_pairs(n))

result = prime_sum_refined(6)
print(result)

assert prime_sum(6) == prime_sum_refined(6)