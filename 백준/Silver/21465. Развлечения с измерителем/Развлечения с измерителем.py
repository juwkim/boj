n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
tu = [set() for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        num = (nums[i][0] - nums[j][0]) ** 2 + (nums[i][1] - nums[j][1]) ** 2
        tu[i].add(num)
        tu[j].add(num)
ans = [num**.5 for num in sorted(tu[0]) if all(num in tu[i] for i in range(1, n))]
print(len(ans))
print(*ans, sep='\n')