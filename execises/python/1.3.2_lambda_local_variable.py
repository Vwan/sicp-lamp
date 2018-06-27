'''f(x,y)=x(1+xy)2+y(1−y)+(1+xy)(1−y),'''

def square(a):
    return a * a

def f1(x, y):
    a = 1 + x * y
    b = 1 - y
    return x * square(a) + y * b + a * b

def f2(x, y):
    def helper(a, b):
        return x * square(a) + y * b + a * b
    return helper(1 + x * y, 1 - y)

def f3(x, y):
     z = lambda a,b:  x * square(a) + y * b + a * b
     return z (1 + x * y, 1 - y)

print (f1(1,2))
print (f2(1,2))
print (f3(1,2))