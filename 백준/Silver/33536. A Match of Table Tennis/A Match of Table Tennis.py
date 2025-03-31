def solve():
    n = int(input())
    score = [0, 0]
    for i, l in enumerate(input().split()):
        s, t = map(int, l.split('-'))
        p, q = sorted((s, t))
        if q == 11 and p <= 9 or q >= 12 and q == p + 2:
            if 3 in score: return 2
            score[t == q] += 1
        elif i != n - 1 or q >= 12 and q >= p + 3:
            return 2
    if s < 10 or t < 10:
        return (s + t & 0x3 > 1) + n & 1
    return s + t + n & 1
print(("HOST", "GUEST", "INCONSISTENT")[solve()])