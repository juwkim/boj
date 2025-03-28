import sys
input = sys.stdin.readline

for _ in range(int(input())):
    SH, SM, DH, DM = map(int, input().split())
    num = -SM
    print("------+---------")
    print(" time | elapsed")
    print("------+---------")
    for i in range(SH, SH + DH + 1 + (SM + DM >= 60)):
        H = i if i <= 12 else i - 12
        if num:
            print(f"{H:2}:XX | XX {'-+'[num > 0]} {abs(num)}")
        else:
            print(f"{H:2}:XX | XX")
        num += 60