def element_of_set(x, set):
    if set is None:
        return False
    else:
        if x in set:
            return True
        else:
            return False

def adjoin_set(x, set):
    if element_of_set(x, set):
        return set
    else:
        set.append(x)
    return set

def intersection_set(set1, set2):
    result = []
    for x1 in set1:
        if element_of_set(x1, set2):
            result.append(x1)
    for x2 in set2:
        if not element_of_set(x2, result) and element_of_set(x2, set1):
            result.append(x2)
    return result

def union_set(set1, set2):
    result = []
    for x1 in set1:
        result.append(x1)
    for x2 in set2:
        result.append(x2)
    return result

set1=list(range(2,10))
set2=list(range(1,5))
print(set1, set2)
assert element_of_set(3, set1) == True
print(adjoin_set(11, set1))

assert set(intersection_set(set1, set2)) == set(set1).intersection(set(set2))

assert set(union_set(set1, set2)) == set(set1).union(set(set2))