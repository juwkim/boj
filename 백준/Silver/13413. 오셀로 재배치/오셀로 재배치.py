for _ in range(int(input())):
    input()
    BW, WB = 0, 0
    for a, b in zip(input(), input()):
        s = a + b
        if s == 'BW':
            BW += 1
        elif s == 'WB':
            WB += 1
    print(max(BW, WB))