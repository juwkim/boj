from decimal import Decimal
alpha = "PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV"
for _ in range(int(input())):
    D = input()
    
    if -1.0 <= Decimal(D) < 1.0:
        dot = D.index('.')

        r = int(D[dot+1:].ljust(16, '0')) // 152587890625
        
        if D[1] != '1' and r == 0:
            dot = 1

        if dot == 2:
            r = (65536 - r) % 65536
            
        bits = ' 01'[dot] + bin(r)[2:].rjust(16, '0')
        buf = []
        buf.append(alpha[int(bits[:5], 2)])
        buf.append(int(bits[5:16], 2))
        buf.append('FD'[int(bits[16])])
        print(*buf)
        
    else:
        print('INVALID VALUE')