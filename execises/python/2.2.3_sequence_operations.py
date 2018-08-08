"""
given a list, enumerate it and filter out all the odds, then add them
"""

def add_odds(lst, total):
    for item in lst:
        if type(item) == list:
            total = add_odds(item, total)
        elif item % 2 != 0:
            total += item * 2
    return total


"""
signal processing:
enumerate
filter
map
add
"""

def add_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

def filter(condition, lst):
    output = []
    for item in lst:
        if condition(item):
            output.append(item)
    return output

def map_list(operation, lst):
    output = []
    for item in lst:
        output.append(operation(item))
    return output

def enumerate_list(lst, output):
    for item in lst:
        if type(item) == list:
            enumerate_list(item, output)
        else:
            output.append(item)
    return output

print(enumerate_list([[1,2],3,4,[5,6]], []))
print(enumerate_list([1,3,4,[5,6]], []))

def sequence_opt(lst):
    new_list = enumerate_list(lst, [])
    filtered_list = filter(lambda x:x%2!=0, new_list)
    mapped_list = map_list(lambda x: x * 2, filtered_list)
    result = add_list(mapped_list)
    print(result)

lst = [[1,2],3,4,[5,6]]
sequence_opt(lst)

print(add_odds(lst, 0))


