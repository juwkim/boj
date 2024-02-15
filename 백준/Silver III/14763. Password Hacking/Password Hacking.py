import sys
input = sys.stdin.readline

buf = []
for _ in range(int(input())):
    password, p = input().split()
    buf.append((float(p), password))
buf.sort(reverse=True)
ans, cur, total = 0, 1, 1
for i, (p, password) in enumerate(buf, 1):
    ans += i * cur * p / total
    cur *= 1 - p / total
    total -= p
print(ans)