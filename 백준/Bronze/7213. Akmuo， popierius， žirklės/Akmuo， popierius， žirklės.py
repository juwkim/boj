a1, p1, z1, a2, p2, z2 = map(int, open(0).read().split())
def solve(l, r, d):
    score = 0
    for i in range(3):
        cnt = min(l[i], r[(i - d) % 3])
        l[i] -= cnt; r[(i - d) % 3] -= cnt
        score += cnt
        if l[i]:
            cnt = min(l[i], r[i])
            l[i] -= cnt; r[i] -= cnt
        if l[i]:
            cnt = min(l[i], r[(i + d) % 3])
            l[i] -= cnt; r[(i + d) % 3] -= cnt
            score -= cnt
    return score
print(solve([a1, p1, z1], [a2, p2, z2], 1))
print(-solve([a1, p1, z1], [a2, p2, z2], -1))