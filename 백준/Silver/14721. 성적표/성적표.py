g = lambda: [*map(int, input().split())]

nums = [g() for _ in range(int(input()))]
buf = [[a, b] for a in range(1, 101) for b in range(1, 101)]
ans = min(buf, key=lambda x: sum((num[1] - x[0] * num[0] - x[1]) ** 2 for num in nums))
print(*ans)