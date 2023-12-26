ans1 = 1
ans2 = 1
input()
s = input()
for a, b in zip(s, s[1:]):
    if a == 'B' and b == 'R':
        ans1 += 1
    if a == 'R' and b == 'B':
        ans2 += 1
print(max(ans1, ans2))