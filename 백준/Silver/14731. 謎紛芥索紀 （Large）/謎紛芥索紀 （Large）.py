import sys
s, t = 0, 10**9 + 7
I = sys.stdin.readline
for _ in range(int(I())):
    C, K = map(int, I().split())
    s += C * K * pow(2, K - 1, t) % t
    if s >= t:
        s %= t
print(s)