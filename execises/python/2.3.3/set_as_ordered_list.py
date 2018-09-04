'''
ordered list as set, ascending
'''

def element_of_set(x, set):
    if set is None or set==[]:
        return False
    else:
        tmp = set[0]
        if x == tmp:
            return True
        elif x < tmp:
            return False
        else:
            set.remove(tmp)
            return element_of_set(x, set)

def adjoin_set(x, set):
    if element_of_set(x, set):
        return set
    if set is None or set == []:
        return [x]
    else:
        if x == set[0]:
            return set
        else:
            for i, index in enumerate(set):
                if x < i:
                    set.insert(index-1, x)
            return set

    return result

def intersection_set(set1, set2):
    result = []
    if set1 == [] or set2 == []:
        return []
    else:
        print(set1, set2)
        x1 = set1[0]
        x2 = set2[0]
        if x1 == x2:
            result.append(x1)
        elif x1 > x2:
            return intersection_set(set1, set2.remove(x2))
        else:
            return intersection_set(set1.remove(x1), set2)

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

set1=list(range(2,10))
set2=list(range(11,15))
print(set1, set2)
assert element_of_set(3, set1) == True
assert element_of_set(11, set1) == False
print(adjoin_set(11, set1))

assert set(intersection_set(set1, set2)) == set(set1).intersection(set(set2)) == set(intersection_set2(set1,set2))
#
# assert set(union_set(set1, set2)) == set(set1).union(set(set2))