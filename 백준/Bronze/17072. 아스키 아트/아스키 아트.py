def intensity(R, G, B):
    I = 2126 * R + 7152 * G + 722 * B
    return '#o+-..'[I//510000]


N, M = map(int, input().split())
for _ in range(N):
    s = [*map(int, input().split())]
    print(''.join([intensity(s[i], s[i+1], s[i+2]) for i in range(0, 3*M, 3)]))