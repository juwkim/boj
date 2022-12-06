cipher = input()
fours = [s for s in cipher.split() if len(s) == 4]
nines = [s for s in cipher.split() if len(s) == 9]

for word in fours:
    move = [(ord(x)-ord(y))%26 for x,y in zip(word[1:],word)]
    if move == [23,13,9]:
        key = (ord(word[0]) - 76) % 26
        break
for word in nines:
    move = [(ord(x)-ord(y))%26 for x,y in zip(word[1:],word)]    
    if move == [5, 1, 7, 23, 8, 19, 23, 8]:
        key = (ord(word[0]) - 67) % 26
        break
    
print(''.join(map(lambda x: [x, chr(65+(ord(x)-key-65)%26)][64<ord(x)<91], cipher)))