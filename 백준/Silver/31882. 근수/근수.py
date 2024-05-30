input()
ans, i = 0, 0
for c in input():
    if c == '2':
        i += 1
    else:
        ans += i * (i + 1) * (i + 2)
        i = 0
ans += i * (i + 1) * (i + 2)
print(ans // 6)