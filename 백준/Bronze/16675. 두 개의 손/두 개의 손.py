ML, MR, TL, TR = input().split()
if ML == MR and 'RSP'[('RSP'.index(ML) - 1) % 3] in [TL, TR]:
    print('TK')
elif TL == TR and 'RSP'[('RSP'.index(TL) - 1) % 3] in [ML, MR]:
    print('MS')
else:
    print('?')