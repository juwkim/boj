from math import comb

a = [input() for _ in range(8)]
i, j, cnt = -1, -1, 0
for x in range(7):
    for y in range(7):
        cur = (a[x][y] == 'O') + (a[x][y+1] == 'O') + (a[x+1][y] == 'O') + (a[x+1][y+1] == 'O')
        if cur > cnt:
            i, j, cnt = x, y, cur
print(i + 1, j + 1)
alive = sum(row.count('O') for row in a)
if alive < cnt + 4:
    print(1)
else:
    print(1 - comb(alive - cnt, 4) / comb(alive, 4))