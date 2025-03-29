import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

dic = defaultdict(set)
cnt = defaultdict(lambda: [0] * 8)
while (s:=input()) != "ENDOFINPUT":
    teller, customer, *time = s.split()
    if customer in dic[teller]:
        dic[teller].remove(customer)
        if time:
            hh = int(time[0][:2])
            if hh < 4: hh += 12
            cnt[teller][hh - 8] += 1
    else:
        dic[teller].add(customer)
for teller in sorted(dic.keys(), key=lambda x: (-sum(cnt[x]), x))[:3]:
    t = (max(range(8), key=lambda x: cnt[teller][x]) + 7) % 12 + 1
    print(f"{teller} {sum(cnt[teller])} {t:02d}{'AP'[t < 4]}M")