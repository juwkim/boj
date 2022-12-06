a = ['000000', '001111', '010011', '011100',
     '100110', '101001', '110101', '111010']
n, s = int(input()), input()
letter = [s[i:i+6] for i in range(0, 6*n, 6)]
encoded, flag = '', 0
for j in range(len(letter)):
    check = [sum(x != y for x,y in zip(letter[j], a[i])) for i in range(8)]
    if check.count(min(check)) > 1:
        flag = 1
        break
    else:
        encoded += 'ABCDEFGH'[check.index(min(check))]
print(j+1 if flag else encoded)