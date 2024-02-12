from collections import*
N,M=map(int,input().split())
print(N*M-sum(max(Counter(l).values())for l in zip(*[input()for _ in' '*N])))