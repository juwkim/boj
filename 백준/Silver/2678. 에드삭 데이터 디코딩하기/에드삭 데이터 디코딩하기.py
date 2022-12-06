from decimal import Decimal
dic = {'P': '00000', 'Q': '00001', 'W': '00010', 'E': '00011', 'R': '00100', 'T': '00101', 'Y': '00110', 'U': '00111', 'I': '01000', 'O': '01001', 'J': '01010', '#': '01011', 'S': '01100', 'Z': '01101', 'K': '01110', '*': '01111', '?': '10000', 'F': '10001', '@': '10010', 'D': '10011', '!': '10100', 'H': '10101', 'N': '10110', 'M': '10111', '&': '11000', 'L': '11001', 'X': '11010', 'G': '11011', 'A': '11100', 'B': '11101', 'C': '11110', 'V': '11111'}
for _ in range(int(input())):
    c, d, s = input().split()
    
    d = int(d)
    num = ''
    while True:
        d, q = divmod(d, 2)
        num = str(q) + num
        if d == 0:
            break
    bits = dic[c] + num.zfill(11) + '01'[s == 'D']
    
    ans = - int(bits[0])
    
    asd = Decimal("0.5")
    for i in range(1, 17):
        if bits[i] == '1':
            ans += asd
        asd /= 2
    
    if ans == int(ans):
        print(str(ans) + '.0')
    else:
        print(ans)