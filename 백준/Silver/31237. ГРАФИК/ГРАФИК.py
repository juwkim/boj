import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
from itertools import combinations
import datetime

off = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday").index(input())
day, monthname = input().split()
day = int(day)
dic = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
month = dic[monthname]
base = datetime.date(2012, 1, 1)
start = datetime.date(2012, 9, 16)
end = datetime.date(2012, month, day)
cnt = [0] * 7
i = off + 1
while start < end:
    cnt[i % 7] += 1
    i += 1
    start += datetime.timedelta(days=1)
ans = 0
X, Y = map(int, input().split())
for l in range(1, 8):
    for c in combinations(range(7), l):
        if X <= sum(cnt[i] for i in c) <= Y:
            ans = c
            break
    else:
        continue
    break
if ans:
    print(len(ans))
    d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in ans:
        print(d[i])
else:
    print(0)