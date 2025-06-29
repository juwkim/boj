import sys
input = sys.stdin.readline

events = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    events.append((a, -1))
    events.append((b, 1))
ans, cur = 0, 0
for pos, delta in sorted(events):
    cur -= delta
    ans = max(ans, cur)
print(ans)