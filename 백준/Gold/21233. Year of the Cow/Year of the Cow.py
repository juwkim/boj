import sys
input = sys.stdin.readline

N, K = map(int, input().split())
buf = set([-1])
for _ in range(N):
    buf.add(int(input()) // 12)
buf = sorted(buf)
s = sorted([b - a - 1 for a, b in zip(buf, buf[1:])], reverse=True)[:K-1]
print((buf[-1] + 1 - sum(s)) * 12)