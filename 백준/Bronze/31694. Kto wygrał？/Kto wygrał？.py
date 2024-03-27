g = lambda: sorted(map(int, input().split()), reverse=True)

def solve():
    a, b = g(), g()
    s, t = sum(a), sum(b)
    if s > t:
        return "Algosia"
    elif s < t:
        return "Bajtek"
    for p, q in zip(a, b):
        if p > q:
            return "Algosia"
        elif p < q:
            return "Bajtek"
    return "remis"
print(solve())