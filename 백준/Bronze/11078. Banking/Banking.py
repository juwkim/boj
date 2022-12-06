try:
    pin = input()
    pattern = input()
            
    buf = []
    ans = 0
    cur = 0
    for c in pattern:
        if c.isupper():
            cnt = ord(c) - 64
        else:
            cnt = ord(c) - 96
            ans += sum(int(pin[i]) for i in range(cur, cur+cnt))
        buf.append(cnt)
        cur += cnt
    
    if sum(buf) == len(pin):
        print(ans)
    else:
        print('non sequitur')
except:
    print('non sequitur')