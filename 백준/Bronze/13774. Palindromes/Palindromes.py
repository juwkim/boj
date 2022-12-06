while (s:=input()) != '#':
    flag = 0
    for i in range(len(s)):
        k = s[:i] + s[i+1:]
        if k == k[::-1]:
            flag = 1
            break
    print(k if flag else 'not possible')