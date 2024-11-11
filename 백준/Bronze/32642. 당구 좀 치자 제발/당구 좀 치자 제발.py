input()
ans, cur = 0, 0
for num in map(int, input().split()):
    cur += (-1, 1)[num]
    ans += cur
print(ans)