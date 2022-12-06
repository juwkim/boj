import sys
for n in sys.stdin:
    n = int(n)
    if n: print(n*(n+1)*(n+2)//6)