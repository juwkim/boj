N, M = map(int, input().split())
if 1 <= (N - 1) % (M + 1) <= M:
    ans = "Can win"
else:
    ans = "Can't win"
print(ans)