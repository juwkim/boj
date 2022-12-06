buf = input().split()
H = int(buf[0])
root = (1 << (H + 1)) - 1
if len(buf) == 1:
    print(root)
else:
    S = buf[1]
    r = root
    minus = 1
    for i in range(len(S)):
        minus <<= 1
        r -= minus
    l = r + minus - 1
    
    for i in range(len(S)):
        minus >>= 1
        if S[i] == 'L':
            r += minus
        else:
            l -= minus
    
    print(l)