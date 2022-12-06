g = lambda: [*map(int, input().split())]


N = int(input())
nums = g()
Sum = sum(nums)
Set = set()
for i in range(N):
    Set.add(Sum - nums[i])
print(len(Set))
print(*sorted(Set))