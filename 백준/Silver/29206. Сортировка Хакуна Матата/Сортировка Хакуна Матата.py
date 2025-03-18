n, *m = map(int, open(0).read().split())
ans = []
def solve(i, num):
    if m[i] == num:
        return
    while m[i] != num + 1:
        solve(i, num + 1)
    j = m.index(num)
    m[i], m[j] = m[j], m[i]
    ans.append((i + 1, j + 1))

for i in range(n):
    solve(i, i + 1)
print(len(ans))
for a in ans:
    print(*a)