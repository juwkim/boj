owner = input()
res = {owner}
cnt = 1
for _ in range(int(input())):
    win, lose = input().split()
    if owner == lose:
        owner = win
        cnt += (owner not in res)
        res.add(owner)
print(owner, cnt)