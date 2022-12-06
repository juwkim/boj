while (s:= input())[0] != '0':
    
    ans = 0
    cur = 0
    H, U, D, F = map(int, s.split())
    
    dU = U * F / 100
    while True:
        ans += 1
        cur += U
        U = max(0, U - dU)
        
        if cur > H:
            print('success on day', ans)
            break
        
        cur -= D
        if cur < 0:
            print('failure on day', ans)
            break