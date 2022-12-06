from datetime import date

def solve(y):
    res = 0
    for m in range(1, 13):
        res += date(y, m, 13).weekday() == 4
    return res

cnt = 0
N = int(input())
for y in range(2018, N):
    cnt += solve(y % 400 + 1)
print(cnt)