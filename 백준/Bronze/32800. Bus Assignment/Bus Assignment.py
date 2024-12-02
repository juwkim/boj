import sys
input = sys.stdin.readline

ans, c = 0, 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    c += b - a
    ans = max(ans, c)
print(ans)