cnt = 0
s = input()
for i in range(len(s)):
    cnt += len({s[j:j+i+1] for j in range(len(s)-i)})
print(cnt)