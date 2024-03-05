from math import perm

n = int(input())
if len(set(map(int, input().split()))) == n:
    a = perm(6 - n, 4 - n)
else:
    a = 0
b = 6 ** (4 - n) - a
print(a, b)