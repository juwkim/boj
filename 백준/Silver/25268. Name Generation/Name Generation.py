alpha = ['aeiou', 'bcdfghjklmnpqrstvwxyz']
l = [5, 21]
for i in range(105, 105 + int(input())):
    num = i
    buf = []
    
    mode = 0
    while True:
        num, q = divmod(num, l[mode])
        buf.append(alpha[mode][q])
        mode ^= 1
        if num == 0:
            break
    print(*buf, sep='')