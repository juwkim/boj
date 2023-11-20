N = int(input())
names = [input() for _ in range(N)]
ans = min([name for name in names if len(name) == 3])
print(ans)