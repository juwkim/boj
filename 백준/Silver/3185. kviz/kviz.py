s = input()
a = [(c, '.')[c.isalpha()] for c in s]
print(*a, sep='')
pos = [i for i in range(len(s)) if s[i].isalpha()]
cnt1 = (len(pos) + 1) // 3
for i in pos[:cnt1]:
    a[i] = s[i]
print(*a, sep='')
revealed = False
for i in pos[cnt1:]:
    if s[i] in "aeiouAEIOU":
        a[i] = s[i]
        revealed = True
if not revealed:
    cnt2 = (2 * len(pos) + 1) // 3
    for i in pos[cnt1:cnt2]:
        a[i] = s[i]
print(*a, sep='')