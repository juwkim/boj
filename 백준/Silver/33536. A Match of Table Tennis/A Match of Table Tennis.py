def solve():
    n = int(input())
    l = input().split()
    a, b = 0, 0
    for i, s in enumerate(l):
        s, t = map(int, s.split('-'))
        if (s == 11 and t <= 9) or (s >= 12 and t == s - 2):
            if a == 3 or b == 3:
                return "INCONSISTENT"
            a += 1
        elif (t == 11 and s <= 9) or (t >= 12 and s == t - 2):
            if a == 3 or b == 3:
                return "INCONSISTENT"
            b += 1
        elif i != n - 1 or (s >= 12 and s - t >= 3) or (t >= 12 and t - s >= 3):
            return "INCONSISTENT"
    if s < 10 or t < 10:
        if (s + t) % 4 < 2:
            return ("HOST", "GUEST")[n & 1]
        return ("GUEST", "HOST")[n & 1]
    else:
        if s + t & 1:
            return ("GUEST", "HOST")[n & 1]
        return ("HOST", "GUEST")[n & 1]
print(solve())