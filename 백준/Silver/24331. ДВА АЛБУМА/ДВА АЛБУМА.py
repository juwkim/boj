g = lambda: map(int, input().split())

n, m = g()
ans = set(g()) & set(g())
print(len(ans))
print(*sorted(ans))