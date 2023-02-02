cnt = [0]
for i in range(9):
    cnt.append(cnt[-1] * 9 + pow(10, i))
    
while int(N:=input()):
    print(f'{N}:', end=' ')
    four = 0
    
    for idx, c in enumerate(N[::-1]):
        four += cnt[idx] * int(c)
        if c > '4':
            four += 10 ** idx - cnt[idx]
    print(int(N) - four)