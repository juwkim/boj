while True:
    a, b, c = sorted(map(float, input().split()))
    if a + b + c == 0:
        break
    if a < 0.25 or b < 90 or c < 125:
        print('not mailable')
    elif a <= 7 and b <= 155 and c <= 290:
        print('letter')
    elif a <= 50 and b <= 300 and c <= 380:
        print('packet')
    elif 2 * a + 2 * b + c <= 2100:
        print('parcel')
    else:
        print('not mailable')