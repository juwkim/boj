ans = 'NO'
s = input()
idx = s.find('-')
if idx != -1:
    a, b = s[:idx], s[idx+1:]
    if 1 < len(a) <= 8 and 1 <= len(b) <= 24:
        ans = 'YES'
print(ans)