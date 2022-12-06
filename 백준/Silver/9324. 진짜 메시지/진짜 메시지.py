for _ in range(int(input())):
    buf = [0] * 26
    ans = 'OK'
    s = input()
    flag = None
    for i in range(len(s)):
        idx = ord(s[i]) - 65
        if flag != None:
            if flag != idx:
                ans = 'FAKE'
                break
            buf[idx] = 0
            flag = None
        else:
            buf[idx] += 1
            if buf[idx] == 3:
                flag = idx
            else:
                flag = None
    if flag != None:
        ans = 'FAKE'
    print(ans)