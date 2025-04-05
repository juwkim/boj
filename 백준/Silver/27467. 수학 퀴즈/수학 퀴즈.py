dp, dq = (0, 1, -1), (1, 0, -1)
p, q = 0, 0
for A in [*open(0)][1].split():
    r = int(A) % 3
    p += dp[r]
    q += dq[r]
print(p, q)