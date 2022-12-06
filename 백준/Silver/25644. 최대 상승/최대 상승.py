g = lambda: [*map(int, input().split())]

n = int(input())
Min = 1e10
ans = 0
for num in g():
    if num < Min:
        Min = num
    else:
        ans = max(ans, num - Min)
print(ans)