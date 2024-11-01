import sys
input = sys.stdin.readline

x, y = 0, 0
ans = 'yes'
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < x or b < y:
        ans = 'no'
        break
    x, y = a, b
print(ans)