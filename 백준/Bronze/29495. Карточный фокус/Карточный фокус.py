from math import log

n, m = map(int, input().split())
i = log(n, m)
print(int(i) + (not i.is_integer()))