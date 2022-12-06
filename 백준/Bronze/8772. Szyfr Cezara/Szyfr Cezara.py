I=input
for _ in[0]*int(I()):
    _,s=I(),I()
    K=(ord(s[0])-ord(I()))%26
    print(''.join(map(lambda s:chr(97+(ord(s)-97-K)%26),s)))