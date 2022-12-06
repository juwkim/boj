import sys
input = lambda: sys.stdin.readline().rstrip('\n')



g = lambda: [*map(int, input().split())]

buf = []
for _ in range(int(input())):
    s, t = g()
    buf.append(t)

ans = 1
s = buf.pop()
while buf:
    t = buf.pop()
    if t <= s:
        s = t
        ans += 1
print(ans)