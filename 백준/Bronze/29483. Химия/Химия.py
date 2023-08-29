dic = {'H': 1, 'C': 12, 'N': 14, 'O': 16}
ans, s = 0, input()
i = 0
while i < len(s):
    if i + 1 < len(s) and s[i + 1].isnumeric():
        ans += dic[s[i]] * int(s[i + 1])
        i += 2
    else:
        ans += dic[s[i]]
        i += 1
print(ans)