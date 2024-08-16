import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

ans = []
N = int(input())
if N:
    A, B = g()
    for i in range(1, N):
        NA, NB = g()
        if (A - B) % 12 == 7 and (NA - NB) % 12 == 7 and A != NA and B != NB:
            ans.append(i)
        A, B = NA, NB
if ans:
    print(*ans, sep='\n')
else:
    print("POLE")