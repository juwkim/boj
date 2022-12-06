def EX(W, L):
    r = (1 - p) / p

    rW = pow(r, W)
    rL = pow(r, -L)

    p0 = (1 - rL) / (rW - rL)
    EWL = W * p0 - (1 - x) * L * (1 - p0)
    return EWL


x, p = input().split()
x = float(x) / 100
p = float(p) / 100
bestwin = 1
ans = 0

win = 0
loss = 1
if p:
    while True:
    
        prev = 0
        flag = False
        
        win = bestwin
        
        while True:
            cur = EX(win, loss)
            if cur > ans:
                ans = cur
                bestwin = win
                flag = True
            
            if cur < prev:
                break
            prev = cur
            win += 1
        
        if not flag:
            break
        loss += 1
print(ans)