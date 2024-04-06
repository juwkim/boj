N, M = map(int, input().split())
ans = 1
for i in range(2, N + 1):
    ans = ans * i % M
    if ans == 0:
        break
print(ans)