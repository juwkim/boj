R, C, ZR, ZC = map(int, input().split())
paper = [input() for _ in range(R)]
for i in range(R):
    for _ in range(ZR):
        for cha in paper[i]:
            print(cha * ZC, end='')
        print()