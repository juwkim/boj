import sys
input = sys.stdin.readline

ans = 0
D, V = 0, 0
for _ in range(int(input())):
    d, v = map(int, input().split())
    V += v
    ans = max(ans, V - D)
    D += d
print(ans)