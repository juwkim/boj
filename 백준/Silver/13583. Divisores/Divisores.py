A, B, C, D = map(int, input().split())
ans = 1e9
for i in range(1, int(C**.5) + 1):
    j, r = divmod(C, i)
    if r: continue
    if i % A == 0 and i % B and D % i: ans = min(ans, i)
    if j % A == 0 and j % B and D % j: ans = min(ans, j)
if ans == 1e9: ans = -1
print(ans)