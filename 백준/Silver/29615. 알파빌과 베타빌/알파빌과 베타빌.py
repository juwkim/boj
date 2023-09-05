g = lambda: [*map(int, input().split())]

N, M = g()
nums = g()
friends = set(g())

ans = sum(num not in friends for num in nums[:M])
print(ans)