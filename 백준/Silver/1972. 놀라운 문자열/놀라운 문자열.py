import sys
input = lambda: sys.stdin.readline().rstrip()

while (s:=input()) != '*':
    ans = f"{s} is surprising."
    for i in range(1, len(s)):
        check = set()
        for j in range(len(s) - i):
            t = s[j] + s[j + i]
            if t in check:
                ans = f"{s} is NOT surprising."
                break
            check.add(t)
        else:
            continue
        break
    print(ans)