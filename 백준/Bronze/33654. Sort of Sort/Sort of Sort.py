input()
ans = []
for a in map(int, input().split()):
    if not ans or a >= ans[-1]:
        ans.append(a)
print(*ans)