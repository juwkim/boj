n = int(input())
def solve(a, b, l):
    print(f"{n}={'+'.join(l + [str(a)])}")
    for i in range(b, a + 1):
        if a - i >= i + 2:
            solve(a - i, i + 2, l + [str(i)])
solve(n, 1, [])