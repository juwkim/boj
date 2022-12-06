while'E'!=input()[0]:
    print(''.join(map(lambda s:[s,chr(65+(ord(s)-70)%26)][64<ord(s)<91],input())))
    input()