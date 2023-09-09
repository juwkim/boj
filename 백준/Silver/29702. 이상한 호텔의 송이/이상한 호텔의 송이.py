for _ in range(int(input())):
    b = bin(int(input()))[2:]
    num = int(b[1:], 2) + 1
    for floor in range(len(b), 0, -1):
        print(f"{floor}{num:018d}")
        num = (num + 1) // 2