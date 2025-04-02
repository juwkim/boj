import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    l = len(p:=input())
    s, cnt = "", 0
    for i in range(l):
        if p[i] == p[-1-i]:
            cnt += 1
        else:
            if cnt > len(s): s = p[i-cnt:i]
            cnt = 0
    if cnt > len(s): s = p[l-cnt:]
    print(s)