from collections import defaultdict

n, a, b, c = map(int, input().split())
d = defaultdict(lambda: n)
def solve(num, i, j, k):
    d[(i, j, k)] = num
    if i < a and d[(i + 1, j, k)] > num // 2:
        solve(num // 2, i + 1, j, k)
    if j < b and d[(i, j + 1, k)] > (num + 1) // 2:
        solve((num + 1) // 2, i, j + 1, k)
    if k < c and d[(i, j, k + 1)] > max(0, (num - 1) // 2):
        solve(max(0, (num - 1) // 2), i, j, k + 1)
solve(n, 0, 0, 0)
print(d[(a, b, c)])