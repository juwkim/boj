l = [*open(0)]

def is_possible1(C, N, F, T):
    surplus = 0
    for c in C:
        surplus = max(0, F * T + surplus - c)
    return surplus > 0

def is_possible2(C, N, F, T):
    surplus = 0
    for c in C:
        fill = F * T + surplus
        if c > fill:
            return False
        surplus = fill - c
    return True

for i in range(0, len(l), 2):
    N, F = map(int, l[i].split())
    C = list(map(int, l[i + 1].split()))

    lo, hi = 0, max(c / F for c in C)
    for _ in range(30):
        mid = (lo + hi) / 2
        if is_possible1(C, N, F, mid):
            hi = mid
        else:
            lo = mid
    print(hi, end=' ')

    lo, hi = 0, max(c / F for c in C)
    for _ in range(30):
        mid = (lo + hi) / 2
        if is_possible2(C, N, F, mid):
            hi = mid
        else:
            lo = mid
    print(hi)