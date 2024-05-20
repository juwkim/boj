import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = input()
for _ in range(int(input())):
    l, r = map(int, input().split())
    p = S[l - 1:r]
    ans = max(sum(p[i-j-1] == p[i+j] for j in range(min(i, len(p) - i))) for i in range(1, len(p)))
    print(ans)