from collections import*
import sys
I=sys.stdin.readline
for i in range(int(I())):
    x,y=I(),I()
    a,b=map(Counter,[x,y])
    print(f'Case #{i+1}: {len(x+y)-2*sum(min(a[s],b[s])for s in a if s in b)}')