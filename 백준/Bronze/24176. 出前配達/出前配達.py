while (s:= input()) != '0 0':
    H, W = map(int, s.split())
    a = [[*map(int, input())] for _ in range(H)]
    w = sum(sum(l) for l in a)
    x = sum(sum(row) * idx for idx, row in enumerate(a)) / w
    y = sum(sum(col) * idx for idx, col in enumerate(zip(*a))) / w
    print(x + 1, y + 1)