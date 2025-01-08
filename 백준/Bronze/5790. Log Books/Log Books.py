import sys
input = sys.stdin.readline

def to_num(s):
    hh, mm = map(int, s.split(':'))
    return hh*60 + mm

while N:=int(input()):
    drive, night = 0, 0
    l = [[*map(to_num, input().split())] for _ in range(N)]
    ans = "PASS"
    for sunin, sunend, s, e in l:
        if e - s > 120:
            ans = "NON"
            break
        drive += e - s
        nightdrive = max(0, sunin - s) + max(0, e - sunend)
        if 2 * nightdrive >= e - s:
            night += e - s
        else:
            night += nightdrive
    if drive < 3000 or night < 600:
        ans = "NON"
    print(ans)