a = 34
x = 33
def f(x):
	global a
	a = 2
	print("a in f:", a)
	print("x in f:", x)

print("--a before eval f--", a)
print("--x before eval f--", x)

f(11)


print("--a after eval f--", a)
print("--x after eval f--", x)
