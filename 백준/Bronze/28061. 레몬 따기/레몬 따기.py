N = int(input())
ans = 0
for idx, num in enumerate(map(int, input().split())):
    ans = max(ans, num - (N - idx))
print(ans)