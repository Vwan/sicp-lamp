def factorial(n):
	def iter(result, count, max):
		if count > max:
			return result
		else:
			return iter(result * count, count + 1, max)
	return iter(1, 1, n)	

print(factorial(5))