import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, Q = map(int, input().split())
l = [input().split() for _ in range(K)]
num = int(l[Q - 1][0])
if num:
    ans = {chr(i + 65) for i in range(1, N)}
    for R, P in l:
        if int(R) >= num:
            ans.discard(P)
    print(*sorted(ans))
else:
    print(-1)