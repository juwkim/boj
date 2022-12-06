s = input()
l = len(s)
ans = '{'
for i in range(l-2):
    a = s[i::-1]
    for j in range(i+1, l-1):
        b = s[j:i:-1]
        c = s[:j:-1]
        word = a + b + c
        ans = min(ans, word)
print(ans)