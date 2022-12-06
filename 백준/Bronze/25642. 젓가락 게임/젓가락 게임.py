A, B = map(int, input().split())
while True:
    A, B = 2 * A + B, A + B
    if B >= 5:
        print('yt')
        break
    if A >= 5:
        print('yj')
        break