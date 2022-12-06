g = lambda: [*map(int, input().split())]

n = int(input())
nums = [g() for _ in range(n)]
nums.sort(key=lambda x: (x[0] / 2 ** x[1], x[0]))
for l in nums:
    print(*l)