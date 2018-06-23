'''
Exercise 1.11: A function f is defined by the rule that :
f(n)=n if n<3 and
f(n)=f(n−1)+2f(n−2)+3f(n−3) if n≥3.
Write a procedure that computes f by means of a recursive process.
Write a procedure that computes f by means of an iterative process.
'''

def f_iter(n):
    def iter(a, b, c, n):
        if n == 0:
            return a
        else:
            return iter(b, c, a+b+c, n-1)
    return iter(0, 1, 2, n)

print(f_iter(40))

def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + f(n-2) + f(n-3)

print(f(40))
