def solve():
    n = int(input())
    a, b = 0, 0
    for i, l in enumerate(input().split()):
        s, t = map(int, l.split('-'))
        if (s == 11 and t <= 9) or (s >= 12 and t == s - 2):
            if a == 3 or b == 3:
                return 2
            a += 1
        elif (t == 11 and s <= 9) or (t >= 12 and s == t - 2):
            if a == 3 or b == 3:
                return 2
            b += 1
        elif i != n - 1 or (max(s, t) >= 12 and abs(s - t) >= 3):
            return 2
    if s < 10 or t < 10:
        return (s + t & 0x3 > 1) + n & 1
    return s + t + n & 1
print(("HOST", "GUEST", "INCONSISTENT")[solve()])