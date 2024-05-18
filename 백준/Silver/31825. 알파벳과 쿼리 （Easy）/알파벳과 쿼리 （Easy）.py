import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

N, Q = g()
S = [ord(c) - ord('A') for c in input()]
for _ in range(Q):
    cmd, l, r = g()
    if cmd == 1:
        print(1 + sum(S[i] != S[i-1] for i in range(l, r)))
    else:
        for i in range(l - 1, r):
            S[i] = (S[i] + 1) % 26