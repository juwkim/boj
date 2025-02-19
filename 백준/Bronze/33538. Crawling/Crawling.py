import sys
input = sys.stdin.readline

l = int(input())
n = int(input())
t = float(input())
ans = "DOOMED"
for _ in range(n):
    f, b = map(float, input().split())
    if l / f + l / b < t:
        ans = "HOPE"
        break
print(ans)