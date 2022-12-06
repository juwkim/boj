import sys
from math import factorial
while True:
    n = [*reversed([*map(int, sys.stdin.readline().rstrip('\n'))])]
    if n == [0]:
        break
    print(sum(n[i] * factorial(i+1) for i in range(len(n))))