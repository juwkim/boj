while True:
    try:
        s, t = input().split()
        idx = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    break
        print('Yes' if idx == len(s) else 'No')
    except:
        break