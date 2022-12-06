g = lambda: [*map(int, input().split())]
n, m = g()
res = ['T' + str(i) for i in range(1, 1 + n)]
for _ in range(m):
    a, b = input().split()
    a_pos = res.index(a)
    b_pos = res.index(b)
    if a_pos > b_pos:
        res.insert(a_pos, res.pop(b_pos))
print(*res)