n = int(input())
ans = 0
Min, Max = 1e9 + 1, 1e9 + 1
for num in map(int, input().split()):
    if num > Max:
        Max = num
    else:
        ans = max(ans, Max - Min)
        Min, Max = num, num
ans = max(ans, Max - Min)
print(ans)