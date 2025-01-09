n, *t = map(int, open(0).read().split())
def solve(f):
    cnt = not f(t[-1], t[0])
    for i in range(n - 1):
        cnt += not f(t[i], t[i + 1])
    return cnt <= 1

if solve(lambda a, b: a >= b) or solve(lambda a, b: a <= b):
    print("TAK")
else:
    print("NIE")