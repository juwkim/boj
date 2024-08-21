import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

cnt = {i: 4 for i in range(1, 14)}
n = int(input())
john = 0
for num in g():
    cnt[num] -= 1
    john += min(num, 10)
mary = 0
for num in g():
    cnt[num] -= 1
    mary += min(num, 10)
common = 0
for num in g():
    cnt[num] -= 1
    common += min(num, 10)
john += common
mary += common
ans = -1
for i in range(1, 14):
    if cnt[i] == 0:
        continue
    score = min(i, 10)
    if mary + score > 23:
        break
    if mary + score == 23 or john + score > 23:
        ans = score
        break
print(ans)