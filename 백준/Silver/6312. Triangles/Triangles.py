tc = 1
while N := int(input()):
    triangle = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(2 * N - 1 - i):
            num = 0
            line, off = 0, 0
            if (i + j) & 1:
                while i + line < N and triangle[i + line][j - off : j + off + 1] == '-' * (2 * off + 1):
                    num += 2 * off + 1
                    line += 1
                    off += 1
            else:
                while i - line >= 0 and triangle[i - line][j - off : j + off + 1] == '-' * (2 * off + 1):
                    num += 2 * off + 1
                    line += 1
                    off += 1
            ans = max(ans, num)
    print(f'Triangle #{tc}')
    print(f'The largest triangle area is {ans}.\n')
    
    tc += 1