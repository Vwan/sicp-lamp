def hello(name):
    return f"hello {name}"

def log(func, name):
    print(func(name))

log(hello, "0....me")

def log1(func, name):
    return func(name)

# log1(hello("hello")) #error
print(log1(hello, "1-----me"))

def log2(func, name):
    '''embedded functions inside log'''
    def internal():
        return "Result is:" + func(name)
    return internal()

print(log2(hello,"2-----me"))

def log3(func):
    '''embedded functions inside log'''
    def internal(name):
        return "Result is:" + func(name)
    return internal
hello = log3(hello)
print(hello("3-----me again"))

def log4(func):
    '''embedded functions inside log'''
    def internal(*args, **kargs):
        return "Result is:" + func(*args, **kargs)
    return internal
hello = log4(hello)
print(hello("4-----me again"))

@log3
def hello5(name):
    return f"hello: {name}"

print(hello5("5-----me again again"))