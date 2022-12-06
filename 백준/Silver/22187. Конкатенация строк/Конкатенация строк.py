ans = []
s = input()
for word in s.split(')'):
    i = 0
    while i < len(word) and word[i] != '(':
        ans.append(word[i])
        i += 1
    ans.append(word[i+1:][::-1])
print(''.join(ans))