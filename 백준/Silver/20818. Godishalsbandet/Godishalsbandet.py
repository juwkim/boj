s = input()
l = len(s) // 2
s += s[:l-1]
ans = s.count('B', 0, l)
cur = ans
for i in range(1, 2*l):
    cur += (s[i+l-1] == 'B') - (s[i-1] == 'B')
    ans = max(ans, cur)
print(ans)