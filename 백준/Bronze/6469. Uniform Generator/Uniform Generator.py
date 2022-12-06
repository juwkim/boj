import sys
for l in sys.stdin:
    s,m=map(int,l.split())
    a=[0]
    for _ in[0]*(m-1):a+=[(a[-1]+s)%m]
    print(f'{s:>10}{m:>10} {"GBoao"[sorted(a)!=[*range(m)]::2]}d Choice\n')