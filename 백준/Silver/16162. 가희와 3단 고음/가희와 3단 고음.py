g = lambda: [*map(int, input().split())]
N, A, D = g()
ans = 0
for num in g():
    if num == A:
        A += D
        ans += 1
print(ans)