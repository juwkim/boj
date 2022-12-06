while True:
    M, A, B = map(int, input().split())
    if (M, A, B) == (0, 0, 0):
        break
    t = M * (1/A - 1/B)
    print(f'{int(t)}:{int(t%1*60):#02d}:{round(t%1*60%1*60):#02d}')