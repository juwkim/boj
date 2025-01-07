import sys
input = lambda: sys.stdin.readline().rstrip()

while (s1:=input()) != ".":
    s2 = input()
    ans = "DIFFERENT"
    if s1 == s2:
        ans = "IDENTICAL"
    else:
        p, q = s1.split('"'), s2.split('"')
        if len(p) == len(q):
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
    print(ans)