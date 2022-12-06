s = input()
flag = 0
for i in range(len(s), 0, -1):
    for j in range(len(s) + 1 - i):
        if s[j:i+j] == s[j:i+j][::-1]:
            flag = i
            break
    if flag:
        break
print(flag)