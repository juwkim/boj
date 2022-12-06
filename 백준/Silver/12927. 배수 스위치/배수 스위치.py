s = [0] + [i == 'Y' for i in input().rstrip()]
ans = -1
cnt = 0
for i in range(1, len(s)):
    if all(state == 0 for state in s):
        ans = cnt
        break
    if s[i]:
        for j in range(i, len(s), i):
            s[j] ^= 1
        cnt += 1
if all(state == 0 for state in s):
    ans = cnt
print(ans)