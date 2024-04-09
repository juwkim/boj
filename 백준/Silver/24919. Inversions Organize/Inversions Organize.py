import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    n = int(input())
    l, r, t, b = 0, 0, 0, 0
    for i in range(2 * n):
        s = input()
        p, q = s[:n].count('I'), s[n:].count('I')
        l += p
        r += q
        if i < n:
            t += p + q
        else:
            b += p + q
    ans = max(abs(l - r), abs(t - b))
    print(f"Case #{tc}: {ans}")