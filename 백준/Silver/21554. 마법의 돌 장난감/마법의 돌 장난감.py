g = lambda: list(map(int, input().split()))

N = int(input())
nums = g()
buf = []
for i in range(N):
    idx = nums.index(i+1)
    nums[i:idx+1] = nums[i:idx+1][::-1]
    buf.append((i+1, idx+1))
print(len(buf))
for line in buf:
    print(*line)