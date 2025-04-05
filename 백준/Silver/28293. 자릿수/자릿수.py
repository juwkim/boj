from math import log10

a, b = map(int, input().split())
print(int(b * log10(a) + 1))