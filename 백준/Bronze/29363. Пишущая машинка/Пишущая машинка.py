def solve(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return i


n = int(input())
ans = len(prv:=input()) + n - 1
for _ in range(n - 1):
    cur = input()
    ans += len(cur) + min(0, len(prv) - 2 * solve(prv, cur) + 1)
    prv = cur
print(ans)