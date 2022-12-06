def token(str):
    lst = []
    alpha = str[0].isalpha()
    i, j = 0, 1
 
    tmp = None
    while j < len(str):
        tmp = str[j].isalpha()
        if alpha != tmp:
            if alpha:
                lst.append(str[i:j])
            else:
                lst.append(int(str[i:j]))
            alpha = tmp
            i = j
        j += 1
    if alpha:
        lst.append(str[i:])
    else:
        lst.append(int(str[i:]))
    return lst
 
 
 
N = int(input())
s = token(input())
for _ in range(N):
    t = token(input())
    i = 0
    end = min(len(s), len(t))
    ans = None
    while i < end:
        if type(s[i]) == type(t[i]):
            if s[i] == t[i]:
                i += 1
            else:
                break
        else:
            if type(s[i]) == str:
                ans = '-'
            else:
                ans = '+'
            break
    if not ans:
        if i == end:
            if len(s) <= end:
                ans = '+'
            else:
                ans = '-'
        else:
            if s[i] < t[i]:
                ans = '+'
            else:
                ans = '-'
    print(ans)