import sys
for _ in range(3):
    N=int(sys.stdin.readline().rstrip())
    S=sum(int(sys.stdin.readline().rstrip())for _ in range(N))
    print(['-','+'][S>0]if S else 0)