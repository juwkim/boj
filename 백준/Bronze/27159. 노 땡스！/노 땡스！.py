N = int(input())
ans = 0
prev = -1
for num in map(int, input().split()):
    if num - prev > 1:
        ans += num
    prev = num
print(ans)