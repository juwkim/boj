def g(x, y):
    if x and x[-1] == y:
        x[-2] += 1
    else:
        x += [1, y]
    return x
    
from functools import reduce
for _ in range(int(input())):
    print(' '.join(map(str, reduce(g, input(), []))))