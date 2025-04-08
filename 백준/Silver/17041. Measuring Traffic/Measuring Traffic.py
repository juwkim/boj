import sys
input = sys.stdin.readline

N = int(input())
segments = []
for _ in range(N):
    op, a, b = input().split()
    segments.append((op, int(a), int(b)))

lo, hi = 0, 1000
for op, a, b in reversed(segments):
    if op == 'on':
        lo = max(0, lo - b)
        hi = max(0, hi - a)
    elif op == 'off':
        lo += a
        hi += b
    else:
        lo = max(lo, a)
        hi = min(hi, b)
print(lo, hi)

lo, hi = 0, 1000
for op, a, b in segments:
    if op == 'on':
        lo += a
        hi += b
    elif op == 'off':
        lo = max(0, lo - b)
        hi = max(0, hi - a)
    else:
        lo = max(lo, a)
        hi = min(hi, b)
print(lo, hi)