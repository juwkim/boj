N, *A = map(int, open(0).read().split())
ans = 0
for i, a in enumerate(sorted(A, reverse=True)):
    if a == 0:
        break
    ans = max(ans, i + a)
print(min(ans, N))