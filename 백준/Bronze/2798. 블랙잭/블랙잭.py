N, M = map(int, input().split())
nums = list(map(int, input().split()))
Max = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            Sum = sum([nums[i], nums[j], nums[k]])
            if Max < Sum <= M:
                Max = Sum
            if Max == M:
                break
        if Sum == M:
            break
    if Sum == M:
        break
print(Max)