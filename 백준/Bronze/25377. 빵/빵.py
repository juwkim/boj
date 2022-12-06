g = lambda: [*map(int, input().split())]
ans = 10000
for _ in range(int(input())):
    A, B = g()
    if A <= B:
        ans = min(ans, max(A, B))
print(-1 if ans == 10000 else ans)