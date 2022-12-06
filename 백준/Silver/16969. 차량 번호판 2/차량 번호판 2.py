mod = 1_000_000_009
s = input()
cur = None
ans = 1
for c in s:
    if c == 'd':
        ans = ans * (10 - (cur == '0')) % mod
        cur = '0'
    else:
        ans = ans * (26 - (cur == 'a')) % mod
        cur = 'a'
print(ans)