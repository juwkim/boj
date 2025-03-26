n, k, *a = map(int, open(0).read().split())
def solve(p):
    b = sorted(num + p * (i & 1) for i, num in enumerate(a))
    m = b[n >> 1]
    return sum(abs(num - m) for num in b)
print(min(solve(k), solve(-k)))