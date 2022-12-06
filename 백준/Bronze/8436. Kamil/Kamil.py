from collections import*
from functools import*
a=Counter(input())
print(reduce(lambda x,y:x*2**a[y],'TDLF',1))