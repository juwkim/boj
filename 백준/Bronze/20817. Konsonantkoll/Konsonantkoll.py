s = input()
ans = s[:2]
count = 1 + (ans[0] == ans[-1])

for i in range(2, len(s)):
    if s[i] == ans[-1] and s[i] in "bcdfghjklmnpqrstvwxz":
        count += 1
    else:
        count = 1
    
    if count < 3:
        ans += s[i]

print(ans)