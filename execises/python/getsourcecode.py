l1=[1,2 ]
l2=[3, 4]

l = zip(l1, l2)

#print(l.__next__())

l = l1.append(l2)

def add(a, b):
    return a + b

import inspect
insp = inspect.getsource(add)
print(insp)
import pandas
print(inspect.getsource(pandas.DataFrame))

from dill.source import getsource, getsourcefile
print(getsource(add))
print(getsource(l1.copy, builtin=True)) #error?
#print(getsource(pandas.DataFrame.append, builtin=True))