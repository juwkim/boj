import sys
input = sys.stdin.readline

s = set()
ans = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a in s or b in s or c in s:
        ans = 1
        break
    s.add(a)
    s.add(b)
    s.add(c)
print(ans)