while True:
    D, RH, RV = map(float, input().split())
    if (D, RH, RV) == (0, 0, 0):
        break
    k = 337**.5/D
    print('Horizontal DPI: %.2f' % (k*RH/16), 'Vertical DPI: %.2f' % (k*RV/9), sep='\n')