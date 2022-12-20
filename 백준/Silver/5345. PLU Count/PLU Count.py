for _ in range(int(input())):
    idx = 0
    for c in input():
        idx += c.lower() == 'plu'[idx % 3]
    print(idx // 3)