ans = ""
s = input()
for i in range(len(s)):
    for j in range(i, len(s)):
        ans = max(ans, s[i:j+1])
print(ans)