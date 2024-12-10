N, M = int(input()), int(input())
cur, check = {}, set([()])
ans = 1
for i, c in zip(map(int, input().split()), input()):
    cur[i] = cur.get(i, 0) + (-1, 1)[c == '+']
    if cur[i] == 0: del cur[i]
    p = tuple(sorted(cur.items()))
    if p in check:
        ans = 0
        break
    check.add(p)
print(ans)