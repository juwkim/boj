import sys
import datetime
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month_dict = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

off = day_names.index(input())
day, month_name = input().split()
month = month_dict[month_name]

date_start = datetime.date(2012, 9, 16)
date_end = datetime.date(2012, month, int(day))

count = [0] * 7
for i, date in enumerate(range((date_end - date_start).days), start=off + 1):
    count[i % 7] += 1

X, Y = map(int, input().split())
for size in range(1, 8):
    for comb in combinations(range(7), size):
        if X <= sum(count[i] for i in comb) <= Y:
            print(size)
            print(*[day_names[i] for i in comb], sep="\n")
            exit()
print(0)