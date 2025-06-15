def solve():
    s, t = input(), input()
    n, m = len(s), len(t)
    if n == m:
        return 1, 1
    P, S = 0, 0
    while P < m and s[P] == t[P]: P += 1
    while P + S < m and s[-1-S] == t[-1-S]: S += 1
    base = sum(map(int, s[P+1:n-S-1]))
    for i in range(P, -1, -1):
        base += int(s[i])
        cur = base
        for j in range(n - S - 1, n):
            cur += int(s[j])
            cur_str = str(cur)
            diff = i + n - 1 - j + len(cur_str) - m
            if diff == 0 and cur_str == t[i:m-n+j+1]:
                return i + 1, j + 1
            if diff < 0:
                break
print(*solve())