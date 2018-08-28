l = [ 1, 2,3,4]
t = 1

def is_symbol_in_list(symbol, list):
    if list is None:
        return False
    elif symbol in list:
        return True
    else:
        return False

print(is_symbol_in_list(t, l))
