import sys
input = sys.stdin.readline

while m:=int(input()):
    w, h = 0, 0
    wcur, hcur = 0, 0
    while (l:=[*map(int, input().split())]) != [-1, -1]:
        if wcur + l[0] <= m:
            wcur, hcur = wcur + l[0], max(hcur, l[1])
        else:
            w, h = max(w, wcur), h + hcur
            wcur, hcur = l
    w, h = max(wcur, w), h + hcur
    print(f"{w} x {h}")