mos = {
    'A': '.-', 'N': '-.',
    'B': '-...', 'O': '---',
    'C': '-.-.', 'P': '.--.',
    'D': '-..', 'Q': '--.-',
    'E': '.', 'R': '.-.',
    'F': '..-.', 'S': '...',
    'G': '--.', 'T': '-',
    'H': '....', 'U': '..-',
    'I': '..', 'V': '...-',
    'J': '.---', 'W': '.--',
    'K': '-.-', 'X': '-..-',
    'L': '.-..', 'Y': '-.--',
    'M': '--', 'Z': '--..',
    '_': '..--', '.': '---.',
    ',': '.-.-', '?': '----'
}
reversed_mos = dict(map(reversed, mos.items()))

for x in range(1, 1+int(input())):
    code = (s:=input()).translate(s.maketrans(mos))
    keys = [len(mos[i]) for i in s]
    i, j, decrypted = 0, 0, ''
    while i+j < len(code):
        i, j = i + j, keys.pop()
        decrypted += reversed_mos[code[i:i+j]]
    print(f'{x}: {decrypted}')