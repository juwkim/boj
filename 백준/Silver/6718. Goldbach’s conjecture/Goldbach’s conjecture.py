import sys
input = sys.stdin.readline

def seive(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]

p = seive(1 << 15)
while n:=int(input()):
    cnt = 0
    l, r = 0, len(p) - 1
    while l <= r:
        if p[l] + p[r] == n:
            cnt += 1
            l += 1
            r -= 1
        elif p[l] + p[r] < n:
            l += 1
        else:
            r -= 1
    print(cnt)