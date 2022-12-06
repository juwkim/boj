g = lambda: [*map(int, input().split())]

N, M = g()

check = lambda: input().replace('0', 'O').replace('1', 'L').replace('2', 'Z').replace('3', 'E').replace('5', 'S').replace('6', 'B').replace('7', 'T').replace('8', 'B')
words = [check() for _ in range(N)]
for _ in range(M):
    a = check()
    if any(word in a for word in words):
        print('INVALID')
    else:
        print('VALID')