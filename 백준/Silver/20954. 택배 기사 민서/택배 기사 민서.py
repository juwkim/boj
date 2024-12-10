for x in[*open(0)][1:]:
    x = int(x)
    if x == 0:
        print(0)
    elif x > 0:
        cnt = (x - 1).bit_length()
        print((1 << cnt + 2) + x - 4)
    else:
        cnt = (-x - 1).bit_length()
        print(6 * (1 << cnt) - x - 4)