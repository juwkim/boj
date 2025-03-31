n = len(s:=input())
a, b = s[::2].count('1'), s[1::2].count('1')
ans, p = 0, 0
for i in range(n):
    num = [a + p, b - p]
    num[i & 1] -= s[i] == '1'
    if num[0] == num[1]:
        ans = i + 1
        break
    if s[i] == '1':
        if i & 1:
            p += 1
        else:
            p -= 1
print(ans)