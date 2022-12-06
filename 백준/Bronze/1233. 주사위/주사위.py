from itertools import*
from collections import*
m=map
print(3+Counter(m(sum,product(*m(range,m(int,input().split()))))).most_common(1)[0][0])