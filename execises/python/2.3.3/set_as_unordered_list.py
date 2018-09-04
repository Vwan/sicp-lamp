'''
unordered list as set
'''

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

def intersection_set2(set1, set2):
    result = []
    for x1 in set1:
        if element_of_set(x1, set2):
            result.append(x1)
    return result

def union_set(set1, set2):
    result = []
    for x1 in set1:
        result.append(x1)
    for x2 in set2:
        result.append(x2)
    return result

set1=[3,2,4,1,5]
set2=[0,2,4,6,5,"s"]
print(set1, set2)
assert element_of_set(3, set1) == True
print(adjoin_set(11, set1))

assert set(intersection_set(set1, set2)) == set(set1).intersection(set(set2)) == set(intersection_set2(set1,set2))

assert set(union_set(set1, set2)) == set(set1).union(set(set2))