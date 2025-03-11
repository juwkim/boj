import sys
input = sys.stdin.readline

def check(d):
    posl, posr = sp - d, sp + d
    time = st
    for p, t in nums:
        diff = t - time
        posl, posr = max(posl - diff, p - d), min(posr + diff, p + d)
        if posl > posr:
            return False
        time = t
    return True

for tc in range(1, 1 + int(input())):
    N = int(input())
    (sp, st), *nums = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: x[1])
    lo, hi = 0, 1000
    while hi - lo > 1e-9:
        d = (lo + hi) / 2
        if check(d):
            hi = d
        else:
            lo = d
    print(f"Case #{tc}: {hi:.9f}")