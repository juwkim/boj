n = len(p := input())

def solve(ch):
    ans, cur = -1e9, 0
    s, e = 1, 1
    for i, c in enumerate(p, 1):
        if cur < 0:
            cur = (-1, 1)[c == ch]
            s = i
        else:
            cur += (-1, 1)[c == ch]
        if cur > ans:
            ans = cur
            e = i
    return ans, s, e

ans1, s1, e1 = solve('R')
ans2, s2, e2 = solve('B')
if ans1 > ans2 or (ans1 == ans2 and s1 < s2):
    print(s1, e1)
else:
    print(s2, e2)