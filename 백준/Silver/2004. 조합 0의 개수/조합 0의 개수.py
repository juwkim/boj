g = lambda: [*map(int, input().split())]

def solve(num, base):
    ret = 0
    while num:
        num //= base
        ret += num
    return ret
n, m = g()

a = solve(n, 5) - solve(m, 5) - solve(n-m, 5)
b = solve(n, 2) - solve(m, 2) - solve(n-m, 2)
ans = min(a, b)
print(ans)