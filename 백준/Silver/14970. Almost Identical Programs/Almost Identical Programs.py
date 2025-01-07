import sys
input = lambda: sys.stdin.readline().rstrip()

while (s1:=input()) != ".":
    s2 = input()
    if s1 == s2:
        ans = "IDENTICAL"
    else:
        cnt = 0
        p, q = s1.split('"'), s2.split('"')
        if len(p) != len(q):
            ans = "DIFFERENT"
        else:
            cnt = 0
            for i, (a, b) in enumerate(zip(p, q)):
                if a == b:
                    continue
                if i & 1:
                    cnt += 1
                else:
                    cnt += 2
                if cnt > 1:
                    break
            if cnt == 1:
                ans = "CLOSE"
            else:
                ans = "DIFFERENT"
    print(ans)