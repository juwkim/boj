import math
from itertools import cycle

def solve(s):
    l = len(s)
    for y in range(1, l // 3 + 1):
        for x in range(l - 3 * y + 1):
            p = s[x:x+y]
            if all(s[i] == c for i, c in zip(range(x, l), cycle(p))):
                return x, y

s = input().split(".")[1]
x, y = solve(s)
a, b = int(s[:x+y]) - int(s[:x] or 0), 10**(x+y) - 10**x
g = math.gcd(a, b)
print(a // g)
print(b // g)