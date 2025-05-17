s = input()
ans = -1
if s[-1] in "aeiouns":
    flag = True
    for i in range(len(s) - 1, -1, -1):
        if s[i] in "aeiou":
            if flag:
                flag = False
            else:
                ans = i + 1
                break
else:
    for i in range(len(s) - 1, -1, -1):
        if s[i] in "aeiou":
            ans = i + 1
            break
print(ans)