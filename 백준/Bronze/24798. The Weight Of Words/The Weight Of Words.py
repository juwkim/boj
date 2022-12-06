l, w = map(int, input().split())
if l <= w <= l * 26:
    r, q = divmod(w, l)
    print(chr(r+97) * q + chr(r+96) * (l - q))
else:
    print('impossible')