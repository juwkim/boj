import sys
input = sys.stdin.readline
from collections import defaultdict

mdays = 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334
while n := int(input()):
    goddess_intervals = []
    cur_g_in = None
    prog_in = {}
    prog_intervals = defaultdict(list)
    for _ in range(n):
        date, t, io, pid = input().split()
        month, day, hour, minute = map(int, (date[:2], date[3:], t[:2], t[3:]))
        now = (mdays[month - 1] + day - 1) * 24 * 60 + hour * 60 + minute
        if pid == "000":
            if io == "I":
                cur_g_in = now
            else:
                if cur_g_in is not None:
                    goddess_intervals.append((cur_g_in, now))
                cur_g_in = None
        elif io == "I":
            prog_in[pid] = now
        else:
            prog_intervals[pid].append((prog_in[pid], now))
    bless = {}
    for pid, intervals in prog_intervals.items():
        total = 0
        for a1, a2 in intervals:
            for b1, b2 in goddess_intervals:
                total += max(0, min(a2, b2) - max(a1, b1))
        bless[pid] = total
    print(max(bless.values()))