g = lambda: [*map(int, input().split())]

check = set()
buf = []
nums = sorted(g())
N = int(input())
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == N:
            two = (nums[i], nums[j])
            if two not in check:
                check.add(two)
                buf.append(two)
for line in buf:
    print(*line)
print(len(buf))