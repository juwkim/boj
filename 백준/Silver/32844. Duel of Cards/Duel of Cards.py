n, *a = map(int, open(0).read().split())
a.sort()
b = sorted({*range(1, 2 * n + 1)} - {*a})
def solve(p, q):
    ans, i = 0, 0
    for num in p:
        while i < n and q[i] < num:
            i += 1
        if i == n:
            break
        ans += 1
        i += 1
    return ans
print(n - solve(a, b), solve(b, a))