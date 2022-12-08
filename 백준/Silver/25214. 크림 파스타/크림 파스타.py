input()
ans, Min = 0, 1e10
for num in map(int, input().split()):
    Min = min(Min, num)
    ans = max(ans, num - Min)
    print(ans, end=' ')