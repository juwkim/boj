g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = 0
buf = []
for i in range(N):
    if nums[i] != i + 1:
        ans += 1
        j = nums.index(i + 1)
        if i:
            nums[i:j+1] = nums[j:i-1:-1]
        else:
            nums[i:j+1] = nums[j::-1]
        buf.append((i+1, j+1))
print(ans)
for line in buf:
    print(*line)