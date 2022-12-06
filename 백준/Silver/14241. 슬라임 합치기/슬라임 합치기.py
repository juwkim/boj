N = int(input())
cur, ans = 0, 0
for num in map(int, input().split()):
    ans += cur * num
    cur += num
print(ans)