import sys
input = lambda: sys.stdin.readline().rstrip()

ZG, GW = [], []
for _ in range(int(input())):
    name, time = input().split()
    start, end = time.split("--")
    hh1, mm1 = map(int, start.split(":"))
    hh2, mm2 = map(int, end.split(":"))
    time1 = hh1 * 60 + mm1
    time2 = hh2 * 60 + mm2
    if name[0] == 'Z':
        ZG.append((time1, time2))
    else:
        GW.append((time1, time2))
ans = 1e9
for s1, e1 in ZG:
    for s2, e2 in GW:
        cnt = (s1 > e1) + (s2 > e2) + (e1 >= s2)
        ans = min(ans, e2 - s1 + 1 + 1440 * cnt)

if ans == 1e9:
    print("NEMOGUCE")
else:
    hh, mm = divmod(ans, 60)
    print(f"{hh}:{mm:02}")