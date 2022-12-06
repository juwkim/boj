from functools import reduce
n, i = input(), 0
while len(n) != 1:
    n = str(reduce(lambda x, y: x*int(y), n, 1))
    i += 1
print(i)