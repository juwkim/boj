ans = 0
x, y = 0, 0
s = input()
for i in range(len(s) - 1):
    if s[i:i+2] == '((':
        x += 1
    elif s[i:i+2] == '))':
        ans += x
print(ans)