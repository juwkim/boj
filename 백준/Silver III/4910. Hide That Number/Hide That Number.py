import sys
input = lambda: sys.stdin.readline().rstrip()

tc = 1
while (s:=input()) != '0':
    ans, prev = [], 0
    for c in map(int, reversed(s)):
        q, r = divmod(c - prev, 10)
        ans.append(r)
        prev = r - q
    if ans[-1] == 0:
        ans = "IMPOSSIBLE"
    else:
        ans = ''.join(map(str, reversed(ans)))
    print(f"{tc}. {ans}")
    tc += 1