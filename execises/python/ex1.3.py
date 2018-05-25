def sum_excl_min(x, y, z):
    min = x
    sum = x * x + y * y + z * z
    if (min > y):
    	min = y    	
    if (min > z):
        min = z
    return min, sum - min * min

print(sum_excl_min(0,0,10))
