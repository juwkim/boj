import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

def solve():
    W, S = g()
    picture = [input() for _ in range(W)]
    stamps = []
    for _ in range(int(input())):
        R, C = g()
        stamps.append([input() for _ in range(R)])
    filled = [bytearray(S) for _ in range(W)]
    for i in range(W):
        for j in range(S):
            if picture[i][j] == '.' or filled[i][j]:
                continue
            for stamp in stamps:
                R, C = len(stamp), len(stamp[0])
                def fill():
                    for off_x in range(R):
                        for off_y in range(C):
                            def can_fill():
                                for x in range(R):
                                    for y in range(C):
                                        p, q = i - off_x + x, j - off_y + y
                                        if p < 0 or p >= W or q < 0 or q >= S:
                                            if stamp[x][y] == '#':
                                                return False
                                            continue
                                        if (p, q) == (i, j) and stamp[x][y] == '.':
                                            return False
                                        if stamp[x][y] == '.':
                                            continue
                                        if picture[p][q] == '.':
                                            return False
                                return True
                            if can_fill():
                                for x in range(R):
                                    for y in range(C):
                                        p, q = i - off_x + x, j - off_y + y
                                        if p < 0 or p >= W or q < 0 or q >= S:
                                            continue
                                        if stamp[x][y] == '.':
                                            continue
                                        filled[p][q] = 1
                                return True
                    return False
                if fill():
                    break
            else:
                return 'NIE'
    return 'TAK'

print(solve())