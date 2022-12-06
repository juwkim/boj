cnt = 1
s = input()
for i in range(len(s)-1):
    cnt += s[i] != s[i+1]
print(cnt//2)