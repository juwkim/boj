g = lambda: [*map(int, input().split())]

N = int(input())
ans, prev = 0, -1
for num in sorted(g()):
    if num - prev > 1:
        ans += num
    prev = num
print(ans)