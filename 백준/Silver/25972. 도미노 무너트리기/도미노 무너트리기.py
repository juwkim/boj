N = int(input())
ans, prev = 0, 0
for a, l in sorted(tuple(map(int, input().split())) for _ in range(N)):
    ans += a > prev
    prev = a + l
print(ans)