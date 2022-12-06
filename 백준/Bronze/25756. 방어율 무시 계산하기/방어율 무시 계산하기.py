ans = 0
input()
for num in map(int, input().split()):
    ans += num / 100 * (1 - ans)
    print(ans * 100)