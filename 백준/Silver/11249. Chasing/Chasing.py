import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, R, T = map(int, input().split())
    ans = (T - R) % N
    if (T - R + 2) % N:
        ans = min(ans, (T - R + 2) % N)
    print(ans)