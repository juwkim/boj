import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    C = [*map(int, input().split())] + [0, 0]
    ans = 0
    for i in range(N):
        while C[i]:
            ans += 1
            C[i] >>= 1
            C[i + 1] >>= 1
            C[i + 2] >>= 1
    print(ans)