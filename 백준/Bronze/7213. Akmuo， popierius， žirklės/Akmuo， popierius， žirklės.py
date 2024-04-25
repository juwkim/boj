a1, p1, z1, a2, p2, z2 = map(int, open(0).read().split())
def solve(l, r, d):
    score = 0
    while sum(l):
        for i in range(3):
            if l[i] == 0:
                continue
            l[i] -= 1
            if r[(i - d) % 3]:
                score += 1
                r[(i - d) % 3] -= 1
            elif r[i]:
                r[i] -= 1
            else:
                r[(i + d) % 3] -= 1
                score -= 1
    return score
print(solve([a1, p1, z1], [a2, p2, z2], 1))
print(-solve([a1, p1, z1], [a2, p2, z2], -1))