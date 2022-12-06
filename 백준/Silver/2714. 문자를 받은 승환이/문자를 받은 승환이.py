alpha = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(int(input())):
    *l, msg = input().split()
    R, C = map(int, l)
    Map = [msg[i:i+C] for i in range(0, R * C, C)]
    
    buf = []
    i, j, d = 0, 0, 0
    
    check = [[0] * C for _ in range(R)]
    for _ in range(R * C):
        buf.append(Map[i][j])
        check[i][j] = 1
        if d == 0:
            if j == C - 1 or check[i][j+1]:
                d = 1
                i += 1
            else:
                j += 1
        elif d == 1:
            if i == R - 1 or check[i+1][j]:
                d = 2
                j -= 1
            else:
                i += 1
        elif d == 2:
            if j == 0 or check[i][j-1]:
                d = 3
                i -= 1
            else:
                j -= 1
        else:
            if i == 0 or check[i-1][j]:
                d = 0
                j += 1
            else:
                i -= 1
    
    ans = []
    for i in range(0, R*C-4, 5):
        ans.append(alpha[int(''.join(buf[i:i+5]), 2)])
    ans = ''.join(ans).strip()
    print(ans)