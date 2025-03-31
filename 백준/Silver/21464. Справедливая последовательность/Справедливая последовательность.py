n = len(s:=input())
a = s[::2].count('1') - s[1::2].count('1')
ans = 0
for i in range(n):
    if a == (1, -1)[i & 1] * (s[i] == '1'):
        ans = i + 1
        break
    if s[i] == '1':
        if i & 1:
            a += 2
        else:
            a -= 2
print(ans)