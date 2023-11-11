n, m = map(int, input().split())
def solve(a, b):
    while a % 2 == 0 and b > a // 2:
        a //= 2
        b *= 2
    return 2 * (a + b)
print(max(solve(n, m), solve(m, n)))