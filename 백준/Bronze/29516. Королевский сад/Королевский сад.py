def solve():
    a, b = map(int, input().split())
    s = [input() for _ in range(a)]
    for i in range(a):
        p = "".join(s[j] for j in range(a) if j != i)
        if len({*p}) <= 1:
            return "Yes"
    s = ["".join(l) for l in zip(*s)]
    for i in range(b):
        p = "".join(s[j] for j in range(b) if j != i)
        if len({*p}) <= 1:
            return "Yes"
    return "No"
print(solve())