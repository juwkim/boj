N, M = map(int, input().split())
ans = "ESCAPE FAILED"
for i, l in enumerate(zip(*[input() for _ in range(N)]), 1):
    if all(c == 'X' for c in l):
        ans = i
        break
print(ans)