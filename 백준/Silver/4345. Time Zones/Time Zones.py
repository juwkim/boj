import sys
input = lambda: sys.stdin.readline().rstrip()

d = {"UTC": 0, "GMT": 0, "BST": 60, "IST": 60, "WET": 0, "WEST": 60, "CET": 60, "CEST": 120, "EET": 120, "EEST": 180, "MSK": 180, "MSD": 240, "AST": -240, "ADT": -180, "NST": -210, "NDT": -150, "EST": -300, "EDT": -240, "CST": -360, "CDT": -300, "MST": -420, "MDT": -360, "PST": -480, "PDT": -420, "HST": -600, "AKST": -540, "AKDT": -480, "AEST": 600, "AEDT": 660, "ACST": 570, "ACDT": 630, "AWST": 480}
for _ in range(int(input())):
    time, *ap, zone1, zone2 = input().split()
    if time == 'midnight':
        t = 0
    elif time == 'noon':
        t = 720
    else:
        hh, mm = map(int, time.split(':'))
        if hh == 12:
            hh = 0
        t = hh * 60 + mm + (0, 720)[ap[0] == "p.m."]
    t = (t + d[zone2] - d[zone1]) % 1440
    if t == 0:
        print("midnight")
    elif t == 720:
        print("noon")
    else:
        hh, mm = divmod(t, 60)
        if hh >= 12:
            hh -= 12
            ap = "p.m."
        else:
            ap = "a.m."
        if hh == 0:
            hh = 12
        print(f"{hh}:{mm:02d} {ap}")