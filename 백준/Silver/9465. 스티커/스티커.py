for _ in range(int(input())):
    n = int(input())
    stickers = [[0] + [*map(int, input().split())] for _ in range(2)]
    for i in range(2, n+1):
        stickers[0][i] += max(stickers[1][i-2:i])
        stickers[1][i] += max(stickers[0][i-2:i])
    print(max(stickers[0][-1], stickers[1][-1]))