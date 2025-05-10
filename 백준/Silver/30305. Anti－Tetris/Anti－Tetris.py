h, w = map(int, input().split())
block = [input() for _ in range(h)]
for i in range(4):
    for j in range(len(block[0])):
        i = 0
        while i < len(block) and block[i][j] == '#':
            i += 1
        if any(block[k][j] == '#' for k in range(i + 1, len(block))):
            break
    else:
        print(len(block), len(block[0]))
        for row in block:
            print(*['#.'[c == '#'] for c in row], sep='')
        break
    block = [l[::-1] for l in zip(*block)]
else:
    print("impossible")