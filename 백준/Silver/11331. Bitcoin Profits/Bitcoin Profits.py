import sys
input = sys.stdin.readline

while N:=int(input()):
    ans = (-1, 0)
    for i, k in enumerate(sorted(map(int, input().split()))):
        ans = max(ans, (k * (N - i), -k))
    print(-ans[1])