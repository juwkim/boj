def right(word):
    for i in range(r):
        for j in range(c):
            if all(word[k] == Map[i][(j + k) % c] for k in range(len(word))):
                return i + 1, j + 1
    return -1, -1

def left(word):
    for i in range(r):
        for j in range(c):
            if all(word[k] == Map[i][(j - k) % c] for k in range(len(word))):
                return i + 1, j + 1
    return -1, -1

def down(word):
    for i in range(r):
        for j in range(c):
            if all(word[k] == Map[(i + k) % r][j] for k in range(len(word))):
                return i + 1, j + 1
    return -1, -1

def up(word):
    for i in range(r):
        for j in range(c):
            if all(word[k] == Map[(i - k) % r][j] for k in range(len(word))):
                return i + 1, j + 1
    return -1, -1

for t in range(1, 1 + int(input())):
    r, c = map(int, input().split())
    Map = [input() for _ in range(r)]

    print(f'Word search puzzle #{t}:')
    for _ in range(int(input())):
        word = input()

        i, j = right(word)
        if i != -1:
            print('R', i, j, word)
            continue

        i, j = left(word)
        if i != -1:
            print('L', i, j, word)
            continue

        i, j = down(word)
        if i != -1:
            print('D', i, j, word)
            continue

        i, j = up(word)
        print('U', i, j, word)
    print()