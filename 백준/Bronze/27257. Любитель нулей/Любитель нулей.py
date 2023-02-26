s = input()
i = 0
while i < len(s) and s[i] == '0':
    i += 1

j = len(s) - 1
while j >= 0 and s[j] == '0':
    j -= 1
print(s[i:j].count('0'))